from itertools import groupby
from collections import Counter

from pycldf.dataset import Dataset


def areality(metadata, feature_id):
    # Read the CLDF Dataset specified by a metadata file:
    grambank = Dataset.from_metadata(metadata)
    for feature in grambank['ParameterTable']:
        if feature['ID'] == feature_id:
            break
    else:
        raise ValueError('unknown Grambank feature ID: {0}'.format(feature_id))

    # Information about macroareas is stored in table with language metadata:
    area_map = {
        l['ID']: (l.get('Macroarea') or '')
        for l in grambank['LanguageTable']}

    # We want to map numeric feature values to more descriptive ones, thus we
    # have to read the value descriptions from the parameters table:
    codes = {c['ID']: c['Description'] for c in grambank['CodeTable']}

    res = Counter()
    for value in grambank['ValueTable']:
        if value['Parameter_ID'] == feature_id:
            # We count the occurrences of each value by (area, code):
            res.update([(
                area_map[value['Language_ID']], 
                codes[value['Code_ID']] if value['Code_ID'] else 'Not known')])
    return feature, res


if __name__ == '__main__':
    import sys

    metadata_path, fid = sys.argv[1:3]
    feature, value_counts_by_area = areality(metadata_path, fid)
    print('\n{0[ID]}: {0[Name]}\n'.format(feature))

    # We count values for each (area, code) pair for the given feature ...
    # ... then group by area ...
    for area, items in groupby(
        sorted(value_counts_by_area.items()),  # Note: groupby requires sorted items.
        lambda p: p[0][0]  # The macroarea is the first component of the key in this dict.
    ):
        if not area:
            # We ignore values for languages with no specified macrarea.
            continue
        print(area)
        items = list(items)  # We want to iterate twice, so we have to cast the generator to a list
        n = float(sum(i[1] for i in items))  # number of all values for this area
        for (_, code), count in items:
            # ... and print out percentages.
            print('  {0}: {1:0.2f}%'.format(code, count / n * 100))
