import collections
from itertools import islice
import pathlib
import re
import shutil
import subprocess

from clldutils.markup import iter_markdown_tables
from cldfbench import Dataset as BaseDataset, CLDFSpec
from pygrambank import Grambank
from pygrambank.sheet import Sheet
from pygrambank.util import iterunique
from pygrambank.contributors import PHOTO_URI, ROLES

from pygrambank.cldf import GlottologGB, BibliographyMatcher
from pygrambank.bib import lgcodestr


# FIXME: These should be fixed in the data!
INVALID = ['9', '.?']
FEATURE_METADATA = collections.OrderedDict((
    ('Grambank_ID_desc', 'Grambank_ID_desc'),
    ('boundness', 'Boundness'),
    ('Flexivity', 'Flexivity'),
    ('Gender/noun class', 'Gender_or_Noun_Class'),
    ('locus of marking', 'Locus_of_Marking'),
    ('word order', 'Word_Order'),
    ('informativity', 'Informativity'),
))


def has_known_glottocode(sheet, glottocodes):
    """Print warning if sheet's glottocode is unknown."""
    if sheet.glottocode in glottocodes:
        return True
    else:
        print('skipping unknown Glottocode:', sheet.path.name)
        return False


def sheet_has_values(sheet, values):
    if values:
        return True
    else:
        print('ERROR: empty sheet', sheet.path.name)
        return False


def create_schema(dataset):
    table = dataset.add_table(
        'contributors.csv',
        'ID',
        'Name',
        'Description',
        {'name': 'Photo', 'valueUrl': PHOTO_URI},
        {
            'name': 'Roles',
            'separator': ', ',
            'datatype': {'base': 'string', 'format': '|'.join(re.escape(r) for r in ROLES)},
        },
    )
    table.common_props['dc:description'] = \
        "Grambank is a collaborative effort. The people listed in this table contributed by " \
        "coding languages or guiding the coding as feature patrons or by facilitating the " \
        "project through funding, technical assitance, etc."
    table.tableSchema.primaryKey = ['ID']

    table = dataset.add_component(
        'LanguageTable',
        {
            'name': 'provenance',
            'dc:description': 'Name of the contributed file',
        },
        {
            'name': 'Family_name',
            'dc:description': 'Name of the top-level language family the variety belongs to',
        },
        {
            'name': 'Family_level_ID',
            'dc:description': 'Glottocode of the top-level language family',
        },
        {
            'name': 'Language_level_ID',
            'dc:description': 'Glottocode of the language-level languoid a variety belongs to - '
                              'in case of doalects',
        },
        'level',
        {
            'name': 'lineage',
            'separator': '/',
            'dc:description': 'list of ancestor groups in the Glottolog classification',
        },
    )
    table.common_props['dc:description'] = "Languageś and dialects for which Grambank has codings."
    table.add_foreign_key('Family_level_ID', 'families.csv', 'ID')

    dataset.add_component(
        'ParameterTable',
        {
            'name': 'Patrons',
            'separator': ' ',
            'dc:description': 'Grambank editors responsible for this feature',
        },
        *FEATURE_METADATA.values(),
    )
    dataset.add_component('CodeTable')
    dataset.add_columns('ValueTable', 'Source_comment', {"name": "Coders", "separator": ";"})
    dataset['ValueTable', 'Value'].null = ['?']
    dataset['ValueTable'].add_foreign_key('Coders', 'contributors.csv', 'ID')
    dataset['ParameterTable'].add_foreign_key('Patrons', 'contributors.csv', 'ID')

    table = dataset.add_table(
        'families.csv',
        'ID',
        'Newick')
    table.tableSchema.primaryKey = ['ID']


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "grambank"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(
            module='StructureDataset',
            dir=self.cldf_dir)

    def cmd_download(self, args):
        subprocess.check_call(
            'git -C {} submodule update --remote'.format(self.dir.resolve()), shell=True)

    def cmd_readme(self, args):
        super_readme = super().cmd_readme(args)
        match = re.fullmatch(
            r'(.*?)(\n## Description\n)(.*?)($|\n##.*)',
            super_readme,
            re.DOTALL)
        before, header, old_desc, after = match.groups()
        desc = [
            '\n![Distribution of classifier languages](map.jpg)',
            old_desc,
            'For examples on how to use this datasets, refer to the',
            '[`recipes` folder in this repository](./recipes/).']
        return '{}{}{}{}'.format(before, header, '\n'.join(desc), after)

    def cmd_makecldf(self, args):
        grambank = Grambank(self.raw_dir / 'Grambank', wiki=self.raw_dir / 'grambank.wiki')

        print('loading language info from glottolog')

        # FIXME: code duplication with pygrambank
        glottolog = GlottologGB(args.glottolog.api)
        languoids_by_glottocode = glottolog.languoids_by_glottocode
        languoids_by_ids = glottolog.languoids_by_ids
        descendants = glottolog.descendants_map

        print('loading bibs')
        bibliography_entries = {}
        bibliography_entries.update(glottolog.bib('hh'))
        bibliography_entries.update(grambank.bib)

        print('computing lang-to-refs mapping ...')
        bibkeys_by_glottocode = collections.defaultdict(set)
        for key, (typ, fields) in bibliography_entries.items():
            for lang_id in lgcodestr(fields.get('lgcode') or ''):
                if lang_id in languoids_by_ids:
                    gc = languoids_by_ids[lang_id].id
                    if gc in descendants:
                        for cl in descendants[gc]:
                            bibkeys_by_glottocode[cl].add(key)
                    else:
                        print('---non-language', lang_id)  # pragma: no cover
        print('... done')

        print('loading data sheets')

        sheets = [
            Sheet(f)
            for f in grambank.sheets_dir.glob('*.tsv')
            if f.name not in grambank.exclude]
        sheets = [s for s in sheets if has_known_glottocode(s, languoids_by_glottocode)]
        sheets = [(s, list(s.iter_row_objects(grambank))) for s in sheets]

        # Chose best sheet for indivdual Glottocodes:
        print('selecting best sheets')
        sheets = list(iterunique(sheets, verbose=True))

        print('collecting data points in data sheets')

        sheets = [
            (s, vals)
            for s, vals in sheets
            if sheet_has_values(s, vals)]

        language_table = [
            collections.ChainMap(
                sheet.metadata(glottolog),
                dict(
                    ID=sheet.glottocode,
                    Name=languoids_by_glottocode[sheet.glottocode].name,
                    Glottocode=sheet.glottocode,
                    provenance=sheet.path.name))
            for sheet, _ in sheets]

        bib_matcher = BibliographyMatcher(
            bibliography_entries,
            bibkeys_by_glottocode)
        for sheet, values in sheets:
            for sheet_row in values:
                # note: this adds bibkeys destructively
                bib_matcher.add_resolved_citation_to_row(
                    sheet.glottocode, sheet_row)
        source_table = [source for source, _ in bib_matcher.get_sources()]

        unresolved = bib_matcher.get_unresolved_citations()
        unresolved.reverse()
        for citation, count in unresolved:  # pragma: no cover
            print(citation, count)
        print(sum(count for _, count in unresolved))

        def coders(sheet, row):
            return sorted(set(sheet.coders).union(row.contributed_datapoint))

        value_table = [
            dict(
                ID='{0}-{1}'.format(row.Feature_ID, sheet.glottocode),
                Language_ID=sheet.glottocode,
                Parameter_ID=row.Feature_ID,
                Code_ID='{0}-{1}'.format(row.Feature_ID, row.Value) if row.Value != '?' else None,
                Value=row.Value,
                Comment=row.Comment,
                Source=row.Source,
                Source_comment=row.Source_comment,
                Coders=coders(sheet, row),
            )
            for sheet, values in sheets
            for row in values
            if row.Value not in INVALID
            and row.has_valid_source()]

        coder_ids = {
            coder
            for dp in value_table
            for coder in dp['Coders']}
        contributor_table = [
            dict(
                ID=c.id,
                Name=c.name,
                Description=c.bio or '',
                Roles=c.roles,
                Photo=c.photo or '')
            for c in grambank.contributors
            if c.should_be_included_despite_no_coding == 'Yes' or c.id in coder_ids]

        # check for typos in coder abbreviations
        contributor_ids = {c['ID'] for c in contributor_table}
        for value in value_table:  # pragma: nocover
            unknown_coders = [
                coder
                for coder in value['Coders']
                if coder not in contributor_ids]
            if unknown_coders:
                raise ValueError('ERROR: {}: unknown coders: {}'.format(
                    value['Language_ID'],
                    unknown_coders))

        print('computing newick trees')

        family_table = {
            ld['Family_level_ID']
            for ld in language_table
            if ld.get('Family_level_ID')}
        family_table = [
            {
                'ID': glottocode,
                'Newick': glottolog.api.newick_tree(
                    glottocode,
                    template='{l.id}',
                    nodes=languoids_by_glottocode),
            }
            for glottocode in family_table]

        print('collecting features and codes')

        gb_features = grambank.features
        parameter_table = [
            collections.ChainMap(
                dict(
                    ID=fid,
                    Name=feature.name,
                    Description=feature.description,
                    Patrons=feature.patrons),
                {colname: feature.get(k, '')
                 for k, colname in FEATURE_METADATA.items()})
            for fid, feature in gb_features.items()]
        code_table = [
            dict(
                ID='{0}-{1}'.format(fid, code),
                Parameter_ID=fid,
                Name=code,
                Description=desc)
            for fid, feature in gb_features.items()
            for code, desc in feature.domain.items()]

        # Create CLDF dataset

        create_schema(args.writer.cldf)

        args.writer.objects['LanguageTable'] = sorted(
            language_table,
            key=lambda r: r['ID'])
        args.writer.objects['ParameterTable'] = sorted(
            parameter_table,
            key=lambda r: r['ID'])
        args.writer.objects['CodeTable'] = sorted(
            code_table,
            key=lambda r: (r['Parameter_ID'], r['Name']))
        args.writer.objects['ValueTable'] = sorted(
            value_table,
            key=lambda r: (r['Language_ID'], r['Parameter_ID']))
        args.writer.objects['contributors.csv'] = sorted(
            contributor_table,
            key=lambda r: r['ID'])
        args.writer.objects['families.csv'] = sorted(
            family_table,
            key=lambda r: r['ID'])

        args.writer.cldf.add_sources(*source_table)

        shutil.copy(
            grambank.wiki / 'FAQ-(general).md',
            args.writer.cldf.directory / 'FAQ.md')

        contribs_md = self.raw_dir.joinpath('Grambank', 'CONTRIBUTORS.md')
        contributors = [
            dict(zip(header, row))
            for header, rows in islice(
                iter_markdown_tables(contribs_md.read_text(encoding='utf8')), 1)
            for row in rows]
        contributors = [
            '{} {} | author'.format(row['First name'], row['Last name'])
            for row in contributors]
        self.dir.joinpath('CONTRIBUTORS.md').write_text(
            '# Contributors\n\nName | Role\n --- | --- \n{}\n'.format('\n'.join(contributors)))

        #if not args.dev:
        self.cldf_reader().validate(log=args.log)
