## Introduction 
Grambank contains 195 features, phrased as questions about the grammatical structure of a language. 189 of these features are binary and have a 'yes' or a 'no' answer. 6 features are multi-valued. All questions can also be answered with 'unknown'. The following are some examples:

| feature number | feature question | possible answers |
| ------------- | ----- | --- | 
| G0B74      | Are there prepositions? | (1) yes, (0) no, (?) unclear/unknown |
| GB196      | Is there a masculine/feminine distinction in second person independent pronouns? | (1) yes, (0) no, (?) unclear/unknown  |
| GB024      | What is the order of numeral and noun in the NP? | (1) numeral-noun, (2) noun-numeral, (3) both, (?) unclear/unknown |
| GB203      | What is the order of the adnominal collective universal quantifier ('all') and the noun? | (1) quantifier-noun, (2) noun-quantifier, (3) both, (0) no universal quantifier, (?) unclear/unknown|

For each language we fill in one value per feature. The possible values for each feature are referred to as the 'value set'. For binary questions the value **1** means 'yes' and the value **0** means 'no'. It is also possible to answer **?**, either (a) if there is information on the feature for a language, but it is unclear what the coding should be, or if (b) there is no information on the feature at all.

Many of the questions have to do with the existence of a marker or construction with a specific function. In these cases a 0 indicates an absence. It can be difficult to clearly confirm an absence when reading linguistic descriptions. That a construction is not mentioned does not always mean that it does not exist. In other words, absence of evidence is not the same as evidence of absence. It could be that an author did not investigate a certain topic because it was not their priority at the time. Or it could be that a feature is so rare in a language that it only comes up in a considerable corpus of natural language data, which we do not have for many languages. Negative responses and uncertainty are treated in further detail [here](https://github.com/grambank/Grambank/wiki/Absence-of-evidence).

For each language, three columns can be filled out: Value, Source, and Comment. For example, Tsafiki (ISO 639-3: cof, Glottolog: colo1256) has morphological cases for pronouns, a feature that is captured with a 1 code for GB071. In the example below, the coder indicated the source they used, including the page numbers (Dickinson 2002: 227-228), and provided a helpful comment that in this language, case is marked by means of enclitics.

| feature number| feature question  | Value  | Source | Comment|
| -------------| -----|-----|-----|-----|
| GB071    | Are there morphological cases for phonologically independent personal pronominal core arguments (i.e. S, A or P)? | 1  | Dickinson 2002: 227-228 | By means of enclitics. |

The source column can only be filled in with values that are valid for the feature. For binary features, that means only **0**, **1** or **?**. For the multistate features, **2**, **3** and **4** are also possible. Only one value is allowed. '1?', for example, is not a valid code.

The source column contains information on the source consulted, with page numbers. If there are no specific page numbers to refer to, for example because a feature is not mentioned in a grammar, this is indicated with 'in passim' instead of the page numbers.

**Information for coders**

When you use a source that is not already indexed in Glottolog, let the reviewer team know when you submit the sheet. If you are familiar with bibTeX, you can add an entry for the reference in [gb.bib](https://github.com/glottobank/Grambank/blob/master/gb.bib). If not, include a basic APA citation for the reference [when you submit the sheet](https://github.com/grambank/Grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-(PR)). You can read more about referencing [here](https://github.com/grambank/Grambank/wiki/Referencing-sources-in-Grambank).

The Grambank feature set covers a wide range of topics, including argument marking (flagging and indexing, alignment and inverse marking), number, gender/noun classes, attributive and predicative possession, counting, TAME, negation, derivation and valency change, predication, interrogation, comparison, relativization, verb classification and word order. Each feature has a unique ID. These numbers identify the order in which features were added and are not ideal for using to sort by if you want to get a thematic order. If you prefer to code using a thematic order, see [this folder](https://github.com/grambank/grambank/blob/master/docs/feature_groupings/feature_grouping_for_coding.csv).

If you have any further problems, please consult [this procedure](https://github.com/grambank/Grambank/wiki/Encountering-coding-problems-and-solving-them).

# General workflow

The following is our procedure for coding new languages. Please see [this page](https://github.com/grambank/grambank/wiki/Revising-existing-coding) for our workflow for revising existing data. These instructions are for internal coders, for external collaborators who want to contribute please see this [article](https://github.com/grambank/grambank/wiki/Contribute).

1. Pick/get assigned a language in the designated to do-lists.
2. [Download a blank coding sheet](https://github.com/grambank/grambank/blob/master/docs/Grambank_most_updated_sheet.tsv)(press the button with an arrow pointing down to a flat line in the top right quadrant of the web-page).
3. Name the file '[your acronym](https://github.com/glottobank/Grambank/blob/master/CONTRIBUTORS.md) + underscore + glottocode + .tsv'.* 
4. Find references to consult. Search the glottocode on Glottolog.org and track down the most suitable sources. You are free to explore other resources outside of Glottolog, for example in your university library or in other repositories online. Use the most extensive and most recent descriptions available. Note that they **must** describe the precise languoid you are coding.
5. Getting access to references. You can use online catalogues, interlibrary loans, etc. to find resources. The node leaders and patrons can also help track down resources which you cannot access on your own, for example by emailing authors or requesting interlibrary loans on your behalf.
6. Code the language. We **strongly** recommend using [LibreOffice Calc](https://www.libreoffice.org/download/download/) to edit spreadsheets. Excel sometimes unpredictably changes the encoding of files, which causes problems when processing the data.
7. Read [the feature descriptions here on this wiki](https://github.com/grambank/grambank/wiki/List-of-all-features) and keep in contact with your node leader and the rest of the community. Do not be afraid to ask questions if the feature description is unclear.
8. You are free to correspond with language experts if you have any questions regarding specific datapoints. See our guidelines for this [here](https://github.com/grambank/grambank/wiki/Interacting-with-experts).
9. Only fill in one value per row, always fill in the source (Author year:pages, [guidelines here](https://github.com/grambank/grambank/wiki/Referencing-sources-in-Grambank)). Remember that everyone can read your comments. The features will sometimes be reordered in the database. This means that you should not refer to other features in the comments, for example, by commenting "see above". For full comment guidelines, go [here](https://github.com/grambank/grambank/wiki/Comments). Make sure that the sheet is saved with tab as field delimiter and " as text delimiter.
10. When encountering problems, contact node leaders and feature patrons, or post an issue in the GitHub repository. You can find more information about how to do this [here](https://github.com/grambank/Grambank/wiki/Encountering-coding-problems-and-solving-them).
11. [Submit finished coding](https://github.com/grambank/Grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-(PR))

\* If you are submitting coding in relation to applying for a Grambank coder position or as [an external person submitting change requests](https://github.com/grambank/grambank/wiki/Contribute), you are welcome to also use other formats besides tsv such as xls, xlsx, csv etc. Internal coders however should only use tsv.

The source you are using should describe the language you are coding. You should not use inference from statements about the language family or about related languages. If we use inference in this manner we distort the data by introducing similarity where it may not be warranted.

All datapoints must have a reference, including question marks.

Once you have submitted the sheet, you can indicate this in the to do list in the appropriate column. This isn't strictly necessary though, as we already know it's submitted through the PR and the to do list is culled via a script. Assigning of languages in the to do list is mainly done so that we don't accidentally work on the same languages and so that the languages that are prioritized are done first.

**See also**

* [Responsibilities for parties involved in GramBank](https://github.com/grambank/Grambank/wiki/Responsibilities-for-parties-involved-in-GramBank)
* [Submitting coding for new languages](https://github.com/grambank/grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-(PR))
* [Referencing source in Grambank](https://github.com/grambank/Grambank/wiki/Referencing-sources-in-Grambank)
* [Revising coding/coding up](https://github.com/grambank/grambank/wiki/Revising-existing-coding)
* [Encountering coding problems and solving them](https://github.com/grambank/Grambank/wiki/Encountering-coding-problems-and-solving-them)
* [Coding strategies, hints and suggestions](https://github.com/grambank/Grambank/wiki/Coding-strategies,-hints-and-suggestions)
* [Absence of evidence](https://github.com/grambank/Grambank/wiki/Absence-of-evidence)
* [Some preliminaries on typology in general as it relates to Grambank](https://github.com/grambank/Grambank/wiki/Some-preliminaries-on-typology-in-general-as-it-relates-to-GramBank)
* [Background of the Grambank questionnaire](https://github.com/grambank/Grambank/wiki/Background-of-the-GramBank-questionnaire)
* [Dependencies between features](https://github.com/grambank/Grambank/wiki/Dependencies-between-features)
* [Recurrent phrasings and concepts](https://github.com/grambank/Grambank/wiki/Recurrent-phrasings-and-concepts)
* [Language internal variation](https://github.com/grambank/grambank/wiki/Language-internal-variation-and-different-strategies-for-one-function)
* [How we learn about the languages' structure so that we might code](https://github.com/grambank/Grambank/wiki/How-we-learn-about-the-languages%E2%80%99-structure-so-that-we-might-code)
* [Interacting with experts](https://github.com/grambank/Grambank/wiki/Interacting-with-experts)
