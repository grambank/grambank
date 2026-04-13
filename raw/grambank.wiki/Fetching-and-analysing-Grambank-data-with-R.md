Within our team we are doing a lot of analysis with the Grambank data, and there are also many outside of our team working with Grambank data. To streamline the workflow and prevent mishaps, the DLCE programmers, Russell Gray and Simon Greenhill have decided on the following recommendations for DLCE-colleagues for getting data and analysing it.

Please remember to cite Grambank, guidelines [here](https://github.com/grambank/grambank/wiki/Citing-grambank).

For more practical guides for using Grambank data, go [here](https://github.com/grambank/grambank/wiki#2-practical-information-for-users-and-collaborators).

For more general information on CLDF, [go here](https://github.com/dlce-eva/dlce-eva/blob/main/doc/cldf_for_dummies.md).

## Project-internal assumptions

* you work on analysis project-wise in dedicated private GitHub reposes, preferably under [Glottobank](https://github.com/glottobank). Later, this repos is made public upon publication of the relevant paper and contains the relevant analysis scripts for your science
* preferably: make the main branch "[protected](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)" to avoid major disruptions
* don't commit too many changes and files in one commit, it makes it harder to tease out what happened and reverse if necessary
* we want to make reproducible science. you want to make sure that future people can re-create all the steps of your work from fetching data, doing analysis, making summaries, plots etc. This means that *all* necessary input data (including what version) should be possible to easily get for another researcher either straight from the codebase (scripts to fetch data, git submodules etc) or by careful documentation and/or is just published straight in the codebase (for example through a zipped SQLlite file, see below). Other users should be able to run all the code on the specified data easily and without errors and disruptions. Ideally, Grambank projects should qualify for [the OSF-badges "Open Data" and "Open Analytical Code"](https://osf.io/tvyxz/wiki/1.%20View%20the%20Badges/).

## Fetching published data from Zenodo
CLDF-data is published continuously on GitHub with separate releases per version ([see here how to view releases on GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags)) and Zenodo ([see here for DOI versioning on Zenodo](https://blog.zenodo.org/2017/05/30/doi-versioning-launched/)). Each version has a unique URL and ID.

If you grab the data via GitHub, make sure to grab a specific version and not just the latest version. For example, [https://github.com/grambank/grambank/tree/master/cldf](https://github.com/grambank/grambank/tree/master/cldf) will update to the most recent state of the remote head of the main branch whereas [https://github.com/grambank/grambank/archive/refs/tags/v1.0.3.zip](https://github.com/grambank/grambank/archive/refs/tags/v1.0.3.zip) points specifically to zipped file of the contents of version 1.0.3. 

The Grambank-project has several GitHub reposes, for an overview go [here](https://github.com/grambank/grambank/wiki/Git-repos-structure). There is a separate one for the clld-app (website), pygrambank, release paper analysis code, etc.

Generally, we recommend fetching published data from Zenodo rather than GitHub as it has DOIs per versions and long-term storage funding.

Each Zenodo dataset has a unique record ID and an associated download link. The link can be obtained by right clicking the button "download" on the web page of any given Zenodo-dataset (see screenshot [here](https://github.com/grambank/grambank/wiki/Fetching-and-analysing-Grambank-data-with-R#fetching-data-zenodo-graphical-user-interface)). Below we use the link to Grambank v1.0.3 `https://zenodo.org/records/7844558/files/grambank/grambank-v1.0.3.zip`.Each release of Grambank has a separate Zenodo entry with a different version number and DOI.

Please note that in recent Zenodo releases, the part of the URL changed from `record` to `records`. Any older links with only "record" will give a `404 (not found)`.

### Fetching data: curl (Command Line)

* Fetch the grambank CLDF data from zenodo e.g. running
   ```shell
   curl -o grambank-v1.0.3.zip https://zenodo.org/records/7844558/files/grambank/grambank-v1.0.3.zip?download=1
   unzip grambank-v1.0.3.zip
   ```

### Fetching data: python package cldfzenodo

Install `cldfzenodo` via
```shell
pip install cldfzenodo
```

Then download the CLDF dataset to a fresh directory:
```shell
$ mkdir gb-v1.0.3
$ cldfbench zenodo.download --directory gb-v1.0.3/ 10.5281/zenodo.7844558
$ tree gb-v1.0.3/
gb-v1.0.3/
├── codes.csv
├── contributors.csv
├── families.csv
├── languages.csv
├── parameters.csv
├── sources.bib
├── StructureDataset-metadata.json
└── values.csv

0 directories, 8 files
```

###  Fetching data: R-package rcldf

The [R-package rcldf](https://github.com/SimonGreenhill/rcldf) is being developed by Simon Greenhill and reads in cldf data correctly as one R-object which contains the tables etc. You can either use a file path to the json of a downloaded CLDF-dataset or use the url of a download link from Zenodo (right click download and copy link URL). Below is an example of the latter with Grambank v1.0.

```
GB <- rcldf::cldf(mdpath = "https://zenodo.org/records/7740140/files/grambank/grambank-v1.0.zip")
```

###  Fetching data: R (other)

You can also read in Zenodo data without rcldf, [example here](https://github.com/HedvigS/personal-cookbook/blob/main/R/download_from_zenodo.R)). Beta-version of function `SH.misc::get_zenodo_dir()` [here](https://github.com/HedvigS/SH.misc/blob/main/R/get_zenodo_dir.R).

### Fetching data: Zenodo Graphical User Interface
You can also click the button "download" on the relevant Zenodo dataset web page.

![Screenshot 2023-11-13 at 14 17 55](https://github.com/grambank/grambank/assets/5327845/5abc8360-8e41-464d-bf0b-1c0f94df29de)


## Next steps


* Document clearly what version you are using - for example in a Makefile, README or other document easily available to a reader/user

* Read the CLDF data from the CSV tables in `grambank-grambank-7ae000c/cldf` or load the data into a SQLite database and access it from there (see below).  `7ae000c` refers to the most recent commit of the relevant version, this will change with each release.


#### Optional: SQLite

* run the `createdb` subcommand from [pycldf](https://github.com/cldf/pycldf)
   ```shell
   cldf createdb grambank-grambank-7ae000c/cldf grambank.sqlite
   ```
   on the unzipped directory, to create a (~94MB) SQLite file "grambank.sqlite". 

* Commit the resulting SQLite file to your GitHub repos (possibly after zipping if it's above GitHub's 100MB file size limit for later versions of Grambank). You can keep scripts for steps 1-4 in your project, but you and other users can from this point use this SQLite file as the starting point for further analysis. By committing it to the repos and including the file in supplementary code etc, the rest of the code you write for the analysis, plotting etc will be executable for any other users as long as it's stored in the same place as the SQLite file.

* Read in the SQLite into R with the package RSQLite (see [example](https://github.com/cldf/cookbook/tree/master/recipes/cldf_r#working-with-cldf-via-sqlite))

There are several reasons for using an SQL interface to the data, one of them is the relationship between the files in a CLDF-dataset and the CLDF-ontology, i.e. is the "LanguageTable" found in the file called "languages.csv"? By making a SQLite file, you can point to files reliably using the ontology-terms and not rely on stable file names. Accessing the data via SQLite will also help unifying the interface for functions in a Grambank R package - see below. Since manipulating (e.g. joining or filtering) data using SQL is very efficient, this will also make it possible to run analyses without the need write/read intermediate data representations to/from files.

## Common Grambank analysis actions

In different projects, we often have to do the same tasks. For example:

* reducing dialects to one/combine dialects
* binarise mutlistate features correctly
* prune EDGE-tree or other phylogenies appropriately
* render theoretical metrics (fusion, informativity etc)

So far we have used ad-hoc solutions, mainly by either copy-pasting scripts from [grambank-analysed](https://github.com/grambank/grambank-analysed) or using grambank-analysed as [a git submodule inside other projects](https://github.blog/2016-02-01-working-with-submodules/). Hedvig Skirgård has developed more generalised R-functions [here](https://github.com/HedvigS/R_grambank_cookbook?tab=readme-ov-file#functions).

**[Basic scripting access](https://github.com/grambank/grambank/blob/master/recipes/README.md)**

**[Table with meta-data on features for analysis (fusion score, informativity etc)](https://github.com/grambank/grambank-analysed/blob/main/R_grambank/feature_grouping_for_analysis.csv)**

**Specific R scripts associated with the release paper (including binarisation and dialect-merging)**
*  [README](https://github.com/grambank/grambank-analysed/blob/main/R_grambank/README.md)
* [make wide and dialect merge](https://github.com/grambank/grambank-analysed/blob/main/R_grambank/make_wide.R)
* [binarise multistate features](https://github.com/grambank/grambank-analysed/blob/main/R_grambank/make_wide_binarized.R)
* [impute missing data in pruned dataset](https://github.com/grambank/grambank-analysed/blob/v1.0/R_grambank/impute_missing_values.R)
* [prune global EDGE-tree](https://github.com/grambank/grambank-analysed/blob/v1.0/R_grambank/spatiophylogenetic_modelling/processing/pruning_EDGE_tree.R)
* [make fusion score](https://github.com/grambank/grambank-analysed/blob/v1.0/R_grambank/make_theo_score_fusion.R)
* [make rest of theoretical scores](https://github.com/grambank/grambank-analysed/blob/v1.0/R_grambank/make_theo_scores.R)
* [make PCA RGD color worldmap](https://github.com/grambank/grambank-analysed/blob/v1.0/R_grambank/PCA/PCA_plot_worldmaps.R)

NB: some scripts require other scripts to be run beforehand. For example, make_wide_binarized.R requires make_glottolog-cldf_table.R and make_wide.R to be run first. You can see run order in the [makefile rules](https://github.com/grambank/grambank-analysed/blob/v1.0/R_grambank/Makefile). If you have questions about grambank-analysed scripts, contact Hedvig Skirgård.

If you are working with specifically [the Gray et al-tree of Austronesian from 2009](https://github.com/D-PLACE/dplace-data/tree/v2.2.1/phylogenies/gray_et_al2009), [here is a script for matching it to the Grambank v1.0 dataset](https://github.com/HedvigS/Oceanic_computational_ASR/blob/v0.1/code/analysis_scripts_gray_mcct/03_get_gray_tree_mcct.R
) ([list of Oceanic duplicates to drop here](https://github.com/HedvigS/Oceanic_computational_ASR/blob/2b898e248dd5c823abfb572b8a117a9b2715794c/code/01_requirements.R#L227
)).

If you use the EDGE-tree by Bockaert et al, please take note to cite:

```
Bouckaert, R., Redding, D., Sheehan, O., Kyritsis, T., Gray, R., Jones, K. E., & Atkinson, Q. (2022). Global language diversification is linked to socio-ecology and threat status. Preprint. https://osf.io/preprints/socarxiv/f8tr6/
```

## Using RCLDF:
rcldf is a package for cldf-manipulation, coordinated by Simon Greenhill. It is not on CRAN, but you can install it directly from GitHub.

Install RCLDF: 

```r
devtools::install_github("SimonGreenhill/rcldf", dependencies = TRUE)
```

```r
> library(rcldf)
> gb <- cldf('grambank/cldf/')
# what tables are there?
> summary(gb)
A Cross-Linguistic Data Format (CLDF) dataset:
Name: Grambank v1.0
Identifier: https://grambank.clld.org
JSON: /Users/simon/Desktop/gb/data/grambank/cldf
Type: http://cldf.clld.org/v1.0/terms.rdf#StructureDataset
Tables:
  1/6: CodeTable (4 columns, 398 rows)
  2/6: contributors.csv (5 columns, 139 rows)
  3/6: families.csv (2 columns, 215 rows)
  4/6: LanguageTable (13 columns, 2467 rows)
  5/6: ParameterTable (12 columns, 195 rows)
  6/6: ValueTable (9 columns, 441663 rows)
Sources: 4241

# get languages:
head(gb$tables$LanguageTable)

# A tibble: 6 × 13
  ID       Name  Macroarea Latitude Longitude Glottocode ISO639P3code provenance
  <chr>    <chr> <chr>        <dbl>     <dbl> <chr>      <chr>        <chr>
1 abad1241 Abadi Papunesia    -9.03    147.   abad1241   NA           JLA_abad1…
2 abar1238 Mung… Africa        6.58     10.2  abar1238   NA           ML_abar12…
3 abau1245 Abau  Papunesia    -3.97    141.   abau1245   NA           MD-GR-RSI…
4 abee1242 Abé   Africa        5.60     -4.38 abee1242   NA           RHE_abee1…
5 aben1249 Aben… Papunesia    15.4     120.   aben1249   NA           SR_aben12…
6 abip1241 Abip… South Am…   -29       -61    abip1241   NA           RHE_abip1…

# get values:
head(gb$tables$ValueTable)

# A tibble: 6 × 9
  ID        Language_ID Parameter_ID Value Code_ID Comment Source Source_comment
  <chr>     <chr>       <chr>        <chr> <chr>   <chr>   <chr>  <chr>
1 GB020-ab… abad1241    GB020        ?     NA      Author… s_OaP… Oa & Paul 201…
2 GB021-ab… abad1241    GB021        ?     NA      Author… s_OaP… Oa & Paul 201…
3 GB022-ab… abad1241    GB022        ?     NA      Author… s_OaP… Oa & Paul 201…
4 GB023-ab… abad1241    GB023        ?     NA      Author… s_OaP… Oa & Paul 201…
5 GB024-ab… abad1241    GB024        2     GB024-2 NA      s_OaP… Oa & Paul 201…
6 GB025-ab… abad1241    GB025        1     GB025-1 NA      s_OaP… Oa & Paul 201…


# get all the data, resolving ID keys:
> df.wide <- as.cldf.wide(gb, 'ValueTable')
```


## Example Makefile

```make

GRAMBANK_VERSION=grambank-v1.0.3.zip

$(shell mkdir -p data)

all: data/grambank.sqlite

### get data
data/$(GRAMBANK_VERSION):
	curl -o $@ "https://zenodo.org/records/7844558/files/grambank/$(GRAMBANK_VERSION)?download=1"

data/grambank/cldf/StructureDataset-metadata.json: data/$(GRAMBANK_VERSION)
	$(shell mkdir -p data/grambank)
	bsdtar -C data/grambank --strip-components=1 -xvf $<

data/grambank.sqlite: data/grambank/cldf/StructureDataset-metadata.json env
	./env/bin/cldf createdb $< $@
	

### bootstrap python
env:
	python -m venv $@
	./$@/bin/python -m pip install --upgrade pip
	./$@/bin/python -m pip install pycldf

### clean: removes auto-generated files
.PHONY: clean
clean:
	rm -rf data env

```

