When coders submit language sheets to Grambank (new or old) we run some python ([pygrambank](https://github.com/grambank/pygrambank)) on them to check for some basic quality conditions. If there are errors or warnings, this is relayed back to the coder and we work to resolve them before merging the coding into the database. There are two pygrambank commands that are run on language coding sheets upon submission to do a basic quality check: `sourcelookup` and `describe` (which calls `check`). The first pertains to the Sources referenced in the sheet and the second to the Value and Comment columns. The python code was written by Robert Forkel and Johannes Englisch, with input from the Grambank patron and node leader team.

We do these checks to ensure that basic small errors that sometimes creep in simply due to human nature are avoided. We value our coders for their expertise in linguistics literature, grammatical jargon, analytical capabilities etc. We understand that typos and errors happen, and this is how we avoid a lot of them in an easy fashion. 

You can also read more about our workflow here:
* [Basics of coding](https://github.com/grambank/grambank/wiki/Basics-of-coding-Grambank)
* [Submitting via GitHub Pull Requests](https://github.com/grambank/grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-(PR))
* [Referencing sources](https://github.com/grambank/grambank/wiki/Referencing-sources-in-Grambank)
* [CLDF and git reposes](https://github.com/grambank/grambank/wiki/CLDF-and-Git-reposes#grambank-cldf)

### describe (check of Value and Comment)
The coding sheet need to satisfy the following conditions:

* the filename is correct (valid coder abbreviation + underscore + valid glottocode .tsv)
* the coding sheet is separated by tabs (not commas)
* the character encoding is UTF8
* there are (at least) four columns named: Feature_ID, Value, Comment and Source
* the values are valid (i.e. 1, 0, ?, 2, 3 depending on feature)
* if the column "Contributed_datapoint" is filled out, it contains valid coder abbreviations
* there are no columns with missing headers
* there are no instances of a Value without a Source, or a Source without a Value

Some combinations of codings are deemed impossible or rare and are flagged as such:

- GB408, GB409, and GB410 can't all be 0
- GB131, GB132, and GB133 can't all be 0
- GB309 can't be 1 if GB083, GB084, GB121 and GB521 are all 0
- if GB022 and GB023 are both 1, these value rows require a comment
- if GB333, GB334, GB335, and GB336 are all 0, these value rows require a comment
- A value of 1 for GB026, GB303, GB320, GB166, GB197, GB129, GB285, GB336, GB260, GB165 or GB319 requires a comment
- If GB256, GB266, and GB273 are all 0, these value rows require a comment.
- If GB072, GB073, GB074, and GB075 are all 0, GB074 and GB075 require a comment.
- If GB155 is 1 and GB113 is 0, both value rows require a comment.
- If GB022 and GB023 are both 0, both value rows require a comment.

For the binarised versions of features, this is the case:

- GB024a and GB024b can't both be 0.
- GB025a and GB025b can't both be 0.
- GB065a and GB065b can't both be 0.
- GB130a and GB130b can't both be 0.

### sourcelookup (check of Source)
Each coding sheet should have a column called "Source". The pygrambank sourcelookup command takes the content in this field (split by semi-colons if more than our source is listed) and attempts to match each source to a bibtex entry in either [gb.bib](https://github.com/glottobank/Grambank/blob/master/gb.bib) or [hh.bib](https://github.com/glottolog/glottolog/blob/master/references/bibtex/hh.bib) (one of glottolog's bibliographies). The match is dependent on author (or editor) name(s) and year. For the match to be successful there needs to be a field in the bibtex-entry called `lgcode` which contains a glottocode or ISO 639-3 code that matches to the glottocode in the filename of the coding sheet. This ensures that we actually match correctly and that there isn't an error in the glottocode in the filename.

If there is more than one publication with the same author(s), year and lgcode we differentiate them by using a unique word from the title. This is done by author_UNIQUE WORD YEAR, for example: `Shaver_relaciones 1982`. 

If the source contains the string "p.c", it is ignored for further scrutiny. It is not matched to an entry in gb.bib or hh.bib.

More details on referencing can be found [here](https://github.com/grambank/grambank/wiki/Referencing-sources-in-Grambank).