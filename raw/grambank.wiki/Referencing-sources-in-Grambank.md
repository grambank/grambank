## Basics

All data-points in Grambank need a source, which is placed in the "source" column of the sheet. This includes data points containing 1, 2, 3, 4, 0 and ?. Sources for ? data-points are all the sources that were consulted. If in the future another sources is published, we should know whether it was considered for this feature or not.

Sources used in Grambank should be formatted as follows:

```
Author and Author and Author YEAR:page(s)
```

For example:

```
Hovdhaugen and Mosel 1992:34
```

## Checks
References in Grambank are checked for
* whether the reference is found in the [hh collection](https://glottolog.org/langdoc/langdocinformation#provider-hh) of Glottolog or in the [bibTeX file for Grambank](https://github.com/grambank/Grambank/blob/master/gb.bib), and
* whether the reference in Glottolog or in the BibTex file is tagged for the same language it is used for in Grambank.

## Avoiding typos
It is easy to make small typos in names and dates. It is a good idea to make a habit of copy pasting the names from the column 'Name' in [Glottolog](https://glottolog.org/langdoc).

## Not in Glottolog hh?
If you use a source that is not (yet) indexed in the hh set of Glottolog, let the reviewer team know when you submit the sheet. If you are familiar with bibTeX, you can add an entry for the reference in [gb.bib](https://github.com/glottobank/Grambank/blob/master/gb.bib). You could also choose to include a basic APA citation for the reference [when you submit the sheet](https://github.com/grambank/Grambank/wiki/Submitting-coding-sheets-via-pull-requests).

## Personal communication
If some of the information in a coding sheet is based on [a discussion with a speaker or a language expert](https://github.com/grambank/grambank/wiki/Interacting-with-experts), they should be cited as follows:

```
Name (p.c. YEAR)'
```

For example:

```
Jeremy Collins (p.c. 2017)
```
## Fieldwork notes (own or others)
If the only source for something is your own or someone else's unpublished fieldwork notes/corpora, write `NAME unpublished field notes (YEAR)`, e.g. `Eri Kashima unpublished field notes (2019)`.


## More than one author
If there is more than one author, their last names should be separated by 'and'. If there is a great number of authors, copy-paste the list of their names as represented in the 'Name' column on [Glottolog](https://glottolog.org/langdoc). It is also possible to use commas for separating multiple authors.

## Page numbers
The page is the page number as represented inside the publication, not the page of a PDF-document. If more than one page is relevant and the page range is continuous, use a dash '-' to indicate the range. For example:

```
Lichtenberk 1979:81-84
```

If you used multiple pages or page ranges that are not continuous, separate them by a comma, for example:

```
Lichtenberk 1979:81, 97
```

It can happen that your coding is not based on a page or a page range, but on a document as a whole. This may be the case because you did not find evidence of a certain phenomenon throughout a book. In those cases, use the phrase 'in passim' instead of page numbers. For example:

```
Lichtenberk 1979:in passim
```

## More than one document by the same author(s) from the same year?
Sometimes an author or a set of authors publish on the same language more than once in the same year. In that case, add an underscore after the author name(s) and enter one or more unique word from the title of the specific resource you are referencing. For example, Shaver published two papers in 1982 on the same language.

* Shaver Swanson, Harold. 1982. Relaciones entre proposiciones en nomatsiguenga. Mary Ruth Wise (ed.), *Conjunciones y otros nexos en tres idiomas amazónicos*: 129-182. Yarinacocha: ILV-SLP-19.
* Shaver Swanson, Harold. 1982. Funciones de la partícula cara en nomatsiguenga. *Serie Lingüística Peruana* 19. 183-197.

In order to separate these two when referencing, use `Shaver_relaciones 1982` and `Shaver_funciones 1982`. That way, our scripts in the back-end can match to the correct bibliographical entries.

## More than one reference per datapoint
If you use multiple sources for one datapoint, separate them with a semicolon `;`. For example:

```
Lichtenberk 1979:in passim; Shaver_relaciones 1982:25; Hovdhaugen and Mosel 1992:34; Jeremy Collins (p.c. 2017)
```

## Citing someone who is citing someone
If you are citing someone who is in their turn getting the information from somewhere else, please cite the source you are reading and put the other information in the comment. For example, if Chan (202023) has information on the numeral system of a certain language and this comes from Mead (2020) you are to put `Chan 2023` as the source and `Mead 2020 via Chan 2023` in the comment field.

If you can locate the secondary source and cite that instead, that is highly preferable. I.e. in the example above it would be good to locate Mead (2020).

The way we deal with sources cannot deal with using the word "via", i.e. `"Mead 2020 via Chan 2023"` in the source field.