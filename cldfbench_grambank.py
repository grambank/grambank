import pathlib

from cldfbench import Dataset as BaseDataset, CLDFSpec
from clldutils.markup import iter_markdown_tables
from pygrambank import Grambank
from pygrambank.cldf import create

CONTRIBUTORS_TMPL = """\
# Contributors

Name | GitHub user | Role
---  | ---         | ---
{}
"""


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "grambank"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(module='StructureDataset', dir=self.cldf_dir)

    def cmd_download(self, args):
        args.log.info('Run "git submodule update --remote" to download the latest raw data')

    def cmd_makecldf(self, args):
        repos = Grambank(self.raw_dir / 'Grambank', wiki=self.raw_dir / 'grambank.wiki')
        create(args.writer.cldf, repos, args.glottolog.api)

        self.cldf_reader().validate(log=args.log)

        header, contribs = next(iter_markdown_tables(
            self.raw_dir.joinpath('Grambank', 'CONTRIBUTORS.md').read_text(encoding='utf8')))
        self.dir.joinpath('CONTRIBUTORS.md').write_text(CONTRIBUTORS_TMPL.format('\n'.join(
            ['{First name} {Last name} | | author'.format(**dict(zip(header, row)))
             for row in contribs])))
