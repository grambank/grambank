Within the Grambank project we have several Git repositories on GitHub. Below is a list of of them, for internal and external use. Not all are public, private ones are only accessible to specific collaborators.

All repositories on GitHub are associated with organisations. The name of a repository on GitHub first consists of the organisation's name and second the name of the specific repository. For example, this wiki exists within the repository `grambank` within the organisation `grambank`. The full name is therefore: `grambank/grambank`. The name of organisations need to be unique all over GitHub, the name of the repository need to be unique within the organisation. Therefore, several repositories can have the same name if they occur in different organisations (e.g. `glottobank/Grambank` and `grambank/grambank`).

### Data locations
* [grambank/grambank](https://github.com/grambank/grambank) - location of published CLDF-releases of Grambank and blank sheet for coders
  * [glottobank/grambank-cldf](https://github.com/glottobank/grambank-cldf) - old location for grambank cldf releases, now **archived**.
* [grambank/grambank.wiki](https://github.com/grambank/grambank/wiki/) - wiki with documentation (linked to grambank/grambank)

### Code associated with specific published papers
* [OlenaShcherbakova/Sociodemographic_factors_complexity](https://github.com/OlenaShcherbakova/Sociodemographic_factors_complexity) - Shcherbakova et al (2023). Societies of strangers do not speak less complex languages. Science Advances, 9(33), eadf7704.
* [grambank/grambank-analysed](https://github.com/grambank/grambank-analysed) - Skirgård et al (2023). Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. Science Advances, 9(16), eadg6175. [Zenodo record of code](https://zenodo.org/records/7740822)
* [HedvigS/Oceanic_computational_ASR](https://github.com/HedvigS/Oceanic_computational_ASR) - Skirgård (in press) Disentangling Ancestral State Reconstruction in historical linguistics: Comparing classic approaches and new methods using Oceanic grammar. Diachronica.
* [NataliiaHue/stability](https://github.com/NataliiaHue/stability) - Hübler, N. (2022). Phylogenetic signal and rate of evolutionary change in language structures. Royal Society Open Science, 9(3), 211252.
* [grambank/gramgaps](https://github.com/grambank/gramgaps) - Lesage et al (2022). Overlooked data in typological databases: What grambank teaches us about gaps in grammars. In 13th Conference on Language Resources and Evaluation (LREC 2022) (pp. 2884-2890). European Language Resources Association (ELRA). (NOT PUBLIC)

### R and python software development
* [HedvigS/rgrambank](https://github.com/HedvigS/rgrambank) - R functions for common Grambank analysis actions
* [grambank/pygrambank](https://github.com/grambank/pygrambank) - python module for grambank quality sanity checks of submitted coding sheets and other tasks
* [SimonGreenhill/rcldf](https://github.com/SimonGreenhill/rcldf) - R package for cldf-dataset handling
* [cldf/cldfbench](https://github.com/cldf/cldfbench) - python module for creating cldf-dataets
* [cldf/pycldf](https://github.com/cldf/pycldf) - python module for cldf-dataset handling

### Non-public internal reposes for project organisation
* [glottobank/Grambank](https://github.com/glottobank) - the everyday raw dataset coders work with continuously (NOT PUBLIC)
* [glottobank/about](https://github.com/glottobank/about) - general repos for glottobank things, including the [paper-captains-document](https://github.com/glottobank/about/blob/master/Papers_plan_captains.md) (NOT PUBLIC)
* [glottobank/ELDP-glottobank](https://github.com/glottobank/ELDP-glottobank) - repos for coordinating coding associated with the Glottobank - ELDP small grants.

## Notes
Please note that Grambank is still actively growing. We're going to make further versions, and we have a to do-list for new languages and for quality control. A language you're looking for might already be in our to do-list or is already included in future releases. Please check with us before coding a new language or revising coding so that we can avoid double work.

Go [here](https://github.com/grambank/grambank/wiki/Fetching-and-analysing-Grambank-data-with-R) for guidelines on fetching Grambank data for analysis in research projects.

For collaborators, check the directory called "original sheets" in glottobank/Grambank for current raw coverage and check the to do-list for what is on its way in.

For more practical guides for using Grambank data, go [here](https://github.com/grambank/grambank/wiki#2-practical-information-for-users-and-collaborators).
