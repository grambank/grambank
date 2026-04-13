# What is Grambank?

Grambank is a global database of structural features of languages. Currently it contains over 2,000 languages and 201 features (195 features if multi-state features are not [binarised](https://github.com/grambank/grambank/wiki/Binarised-features)). It is led by Russell Gray and is a part of the Glottobank-consortium.

# What is the aim of Grambank?

Grambank aims to provide a large amount of typological data on languages, as recorded in grammars and grammar sketches, that can be used to investigate deep language prehistory, geographical and historical grammatical patterns, language universals, cognitive or communicative constraints, the functional interaction of grammatical features and more. 

Grambank is part of [Glottobank](https://glottobank.org/), a research consortium that involves work on complementary databases of lexical data, paradigms, numerals and sound patterns in the world's languages. Grambank can easily be used in concert with other databases to deepen our understanding of our history and communicative capabilities.

# Who is funding it?

The maintenance and collection of data for Grambank is funded by the Department of Linguistic and Cultural Evolution at the Max Planck Institute for Evolutionary Anthropology in Leipzig, Germany. Additional support, such as the hosting of coders, HR admin and the time of researchers, has also been provided by School of Oriental and African Studies in London, Christian-Albrechts-Universität zu Kiel, the Australian National University, the ARC Centre of Excellence for the Dynamics of Language, the University of Colorado Boulder and Uppsala University.

# Will it be updated?

Yes. As we learn more about the languages in our dataset, either by quality-control rechecking of existing data points, spot-checking or feedback from experts or signers/speakers, we will revise and update the dataset so that it is the best it can be. We also continuously add new languages to the dataset.

If you want to contribute to our database by giving us feedback on data, please go to [here](https://github.com/grambank/grambank/wiki/Contribute).

Grambank is a part of the Cross-Linguistic Linked Data-project (CLLD) and is available in Cross-Linguistic Data Format (CLDF). As such, there will continuously be new versions released. As with all CLLD and CLDF-databases, it is important that you note down what version you have used in any analysis of the dataset.

# Why isn't Spanish/German/other language in Grambank?
We are adding new languages continuously, future releases will have more languages in it. We have not focussed much on languages of Europe in our research plans so far, which is why for example Spanish and German are not included in the first release. We read grammars in many different languages, and there is no lack of material available for us to include further languages - we just haven't gotten to them all yet. Grambank version 1.0 has 2,430 languages in it. There are approximately 7,000 languages in the world, and out of those [approximately 4,500 have grammatical descriptions that we can use as source material](https://glottolog.org/langdoc/status). Keep an eye out for future releases. 

# I have found a mistake! How do I help you fix it?
Thank you for wanting to help improve the quality of our data-set. Please let us know [here](https://github.com/grambank/grambank/wiki/Contribute).

# What is the relationship between the World Atlas of Language Structures and Grambank?
The World Atlas of Language Structures was a project between 2000-2013 at the Department of Linguistics at the Max Planck Institute for Evolutionary Anthropology in Leipzig. It consisted of many different scholars who collaborated on a joint database. Each chapter concerns different concepts and variables were coded by the authors of that chapter for a minimal set of 100 languages, and often many more.

Grambank is a project at the Department of Linguistic and Cultural Evolution at the Max Planck Institute for Evolutionary Anthropology in Leipzig. The project design consists of a questionnaire that is filled in as much as possible one language at a time by a set of trained student and research assistants.

The features in WALS and Grambank share similarities, but cannot be translated one-to-one. For example, Grambank contains several binary features asking for strategies for polar interrogation whereas WALS chapter 116 asks what the dominant strategy is.

There are many more similarities and differences between WALS and Grambank, but they can be considered "sister-databases" both in origin and spirit. Read the [WALS chapters](https://wals.info/chapter) and [Grambank feature descriptions](https://github.com/grambank/grambank/wiki/List-of-all-features) to learn more about conceptual differences.

# Why was a new database created instead of expanding WALS?
It was not practical for us to expand WALS because the WALS features were not optimised for the kinds of analysis we want to do and contained significant feature dependencies and consistency problems.

The World Atlas of Language Structures collated a lot of different studies into one anthology. The intended aim was a book with chapters by different authors and helpful maps. The project was not intended to produce data for computational analysis, and there were design choices made that make the data disadvantageous for such analysis. For example, the number of options for each variable was restricted by the number of colours the maps could easily show. The chapters have different authors and they sometimes use different definitions for similar concepts. This leads to a consistency of coding within each chapter, but not necessarily between chapters. The feature set includes significant levels of interdependence, which is a problem for several statistical approaches. There are further differences in the structure of the features that would not be optimal for the research analysis we want to carry out, for example: unlike WALS Grambank avoids "other"-categories and allows languages to be classified into several different types (e.g. if several word orders are pragmatically marked, they can all be coded as present). The current WALS-dataset is sparse, with over 80% missing data. Expanding WALS would mean first filling in these missing data points before new languages could be added, which would in itself take a significant effort. We decided that such an effort was better invested in a feature-set that was better suited for our needs from the start. Therefore, we decided to instead create our own questionnaire, influenced by existing projects - including WALS. You can read more about the history of our questionnaire [here](https://github.com/grambank/grambank/wiki/Background-of-the-Grambank-questionnaire#questionnaire-history). We have adopted a model of data-coding that strives for consistency over languages and over features. We take great efforts to ensure that Grambank-coders apply the concepts consistently, which is why we have detailed descriptions of features and mechanisms in place for dealing with confusion or disagreement such as training, meetings etc.

Lastly, the WALS-project ended in 2013. One of the WALS-editors, Martin Haspelmath, has clearly said that this project is ended and that they are not working on corrections or expansions.

# I want to do analysis with Grambank data, are there python or R-packages I should be aware of?

Yes! Please go [here](https://github.com/grambank/grambank/wiki/Fetching-and-analysing-Grambank-data-with-R).

# How do I cite Grambank?

Like [this](https://github.com/grambank/grambank/wiki/Citing-grambank).

# How does Grambank as a project work?

We describe how the project works in practice in several articles on this wiki:

* [basics of Grambank coding](https://github.com/grambank/grambank/wiki/Basics-of-coding-Grambank)
* [advice for typological database construction](https://github.com/grambank/grambank/wiki/Advice-for-typological-database-construction) 
* [Solving coding problems](https://github.com/grambank/grambank/wiki/Encountering-coding-problems-and-solving-them)
* [conflict resolution](https://github.com/grambank/grambank/wiki/Coding-conflict-resolution)
* See further articles of section 2 & 3 [here](https://github.com/grambank/grambank/wiki#2-practical-information-for-users-and-collaborators)
