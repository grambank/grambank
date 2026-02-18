# Introduction
In our paper "Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss" from 2023, we analysed features of Grambank and also constructed and then analysed a set of metrics derived from Grambank features. These metrics are:

1) Word order 
2) Locus of marking 
3) Fusion
4) Flexivity
5) Noun class/gender
6) Informativity

Each of the above metrics (save informativity) was calculated by assigning values (0, 0.5, and 1) to each Grambank feature that expresses information about the phenomenon captured by that metric, according to the extent to which the feature is consistent or inconsistent with the typological phenomenon. These values can then be used to derive a score for any given language given their Grambank coding. For example, a high Fusion score indicates that a language has much content fused (for example, affixes on nouns instead of free-standing particles for number). These metrics are naturally dependent on the particular features of the Grambank questionnaire and should be understood within that context. For example, there are no features for specific morphological cases - just core versus non-core. 

These metrics have later been used in other publications and have been of interest to other researchers. In order to facilitate the understanding of these and their usage, this wiki article outlines more details. If you are interested in using these metrics in research, please read this wiki article thoroughly. Of special note is [treatment of missing data, as this can impact the scores significantly,](https://github.com/grambank/grambank/wiki/Aggregate-metrics-derived-from-Grambank-data#treatment-of-missing-data), [treatment of `0` and `0.5` weights for Fusion](https://github.com/grambank/grambank/wiki/Aggregate-metrics-derived-from-Grambank-data#variation-in-calculation-of-fusion-score) and [binarised versions of word-order features](https://github.com/grambank/grambank/wiki/Aggregate-metrics-derived-from-Grambank-data#multistate-and-binarised-features) (Grambank version >= 2). 

All metrics (save the word-order metric) consist of partially overlapping features. For example, [GB042 Is there a productive overt morphological singular marker on nouns?](https://github.com/grambank/grambank/wiki/GB042) counts for 1 for Fusion, 1 for Locus of marking and `singular` for Informativity. Below is a plot illustrating the overlap, x-axis is metrics, y-axis Grambank features (v1) and light blue represent that that feature participates in that metric. Features contributing 0 to Fusion have been excluded as they have not been use in analysis yet (for details see [this section](https://github.com/grambank/grambank/wiki/Aggregate-metrics-derived-from-Grambank-data#variation-in-calculation-of-fusion-score)). Features contributing to no metric have been excluded (N = 60).

<img width="610" height="740" alt="GB_parameters_indices" src="https://github.com/user-attachments/assets/23b5a895-ed89-4937-9de9-6ce25fb5ec2d" />

## Origins
These metrics were originally conceived of in order to interpret the Principal Components of the overall Grambank dataset. We noticed that the first three principal components showed some patterns with regards to what features were loading onto which dimension which echoed themes in linguistic typology. In order to evaluate this statistically, as opposed to only relying on informal interpretation of loadings, we constructed a set of metrics that commonly occur in theoretical linguistics. We cast the net wide and included many conceptual dimensions discussed in the linguistic typology literature that we could quantify with our features. We then compared these metrics to the Principal Components and were able to show that PC1 correlates highly with Fusion and PC2 with Noun class/gender. PC3 did not show a strong significant correlation with any of the metrics (see figure below). This work was primarily done by Hannah Haynie and Hedvig Skirgård, based on literature from grammatical typology and theoretical linguistics, with additional significant contributions by Olena Shcherbakova. All metrics, save `Noun class/gender`, were directly inspired by existing linguistics literature.

<img width="769" alt="Screenshot 2025-06-24 at 13 47 29" src="https://github.com/user-attachments/assets/ec771665-22b3-4a32-8d05-a0bdb5543f94" />

Figure S16 from Skirgård et al (2023).

## Practical notes
The basic process is as follows: `Grambank ParameterTable (information of metric values per feature)` + `Grambank ValueTable  (information on data for each language and feature)` = `metric scores per language`. 

Information about the relationship between Grambank features and these metrics are found in the [ParameterTable in the CLDF-version of the dataset](https://zenodo.org/records/7844558) (for more on CLDF, please see [this document](https://github.com/dlce-eva/dlce-eva/blob/main/doc/cldf_for_dummies.md#tables-in-most-cldf-modules). [The R-package rgrambank](https://github.com/HedvigS/rgrambank/blob/main/README.md#functions) can compute these metrics for you given a CLDF Grambank ValueTable and ParameterTable.

### Treatment of missing data
In the Grambank release paper (Skirgård et al 2023), we reduced the entire Grambank data to one subset of languages and features with little missing data and then computed the aggregated metrics, PCA etc. However, a more precise approach is to prune differently for each metric, optimising for optimal coverage for the features involved for the specific metric. The function `rgrambank::make_theo_scores`  prunes for missing data with respect to the specific features involved in each of the metrics. The function also allows the users to define any cut-off (default = 0.75). The difference between the approach in the release paper and the new approach in `rgrambank::make_theo_scores` (0.75 cut-off) is very small in practice. Below are two scatterplots of two central theoretical scores, Fusion and Informativity. In each plot, the x-axis represents the newer way of computing the score (as in `HedvigS/rgrambank`) and the y-axis the older (`grambank/grambank-analysed`) used in Skirgård et al (2023).

<img src="https://github.com/HedvigS/R_grambank_cookbook/assets/5327845/b187b78a-6175-4494-8ae5-499efa96887d" width="300" height="300">
<img src="https://github.com/HedvigS/R_grambank_cookbook/assets/5327845/9e9237d8-b7f5-4dc2-b82e-5d488e152965" width="300" height="300">


# Word order
The metric expresses the degree to which a language uses structures hypothesised to correlate with proposed verb-initial word order patterns (Greenberg 1963; Dryer 1992), given their grambank coding. Each Grambank feature receives a value of 0 or 1, see table below, which is then used to calculate the score for each language.

|ID	|	Name	|	Word_Order	|
|--	|--	|	--	|
|GB022	|	Are there prenominal articles?	|	0	|
|GB023	|	Are there postnominal articles?	|	1	|
|GB024a*	|	Is the order of the numeral and noun Num-N?	|	0	|
|GB024b*	|	Is the order of the numeral and noun N-Num?	|	1	|
|GB025a*	|	Is the order of the adnominal demonstrative and noun Dem-N?	|	0	|
|GB025b*	|	Is the order of the adnominal demonstrative and noun N-Dem?	|	1	|
|GB065a*	|	Is the pragmatically unmarked order of adnominal possessor noun and possessed noun PSR-PSD?	|	0	|
|GB065b*	|	Is the pragmatically unmarked order of adnominal possessor noun and possessed noun PSD-PSR?	|	1	|
|GB074	|	Are there prepositions?	|	1	|
|GB075	|	Are there postpositions?	|	0	|
|GB131	|	Is a pragmatically unmarked constituent order verb-initial for transitive clauses?	|	1	|
|GB133	|	Is a pragmatically unmarked constituent order verb-final for transitive clauses?	|	0	|
|GB193a*	|	Is the order of the adnominal property word (ANM) and noun ANM-N?	|	0	|
|GB193b*	|	Is the order of the adnominal property word (ANM) and noun N-ANM?	|	1	|
|GB203a*	|	Is the order of the adnominal collective universal quantifier (UQ) and noun UQ-N?	|	0	|
|GB203b*	|	Is the order of the adnominal collective universal quantifier (UQ) and noun N-UQ?	|	1	|
|GB262	|	Is there a clause-initial polar interrogative particle?	|	1	|
|GB327	|	Can the relative clause follow the noun?	|	1	|
|GB328	|	Can the relative clause precede the noun?	|	0	|
|GB421	|	Is there a preposed complementizer in complements of verbs of thinking and/or knowing?	|	1	|
|GB422	|	Is there a postposed complementizer in complements of verbs of thinking and/or knowing?	|	0	|
Table 1: Grambank features making up the word order metric.
* See section "Multistate and binarised features".


## Multistate and binarised features
Grambank version 1 contains a set of multistate features (e.g. [GB024 What is the order of numeral and noun in the NP?](https://github.com/grambank/grambank/wiki/GB024)). These are all related to word order and for the computation of the word order metric based on Grambank version 1, we binarised these out such that a value of 1 gives a word order score of 0 and 2 gives 1. A value of 3 for the multistate gives a 1. In Grambank version 2 and further releases, we include coding of languages where the coders coded the binarised version of the feature directly. Therefore, Grambank version 2+ contain both the multistate and binarised version of these features. You can read more about [binarising of multistate features in Grambank here](https://github.com/grambank/grambank/wiki/Binarised-features) and you can use [the R-package rgrambank](https://github.com/HedvigS/rgrambank/blob/main/README.md#functions) to compute this all for you correctly and speedily for both version 1 and further versions.

# Locus of marking
The degree to which a language mainly features head or dependent marking, as described by Nichols (1986). Specifically, the feature-wise metric values reflect consistency with proposed head marking patterns.

|	ID	|	Name	|	Locus_of_Marking	|
|--	|--	|	--	|
|	GB042	|	Is there productive overt morphological singular marking on nouns?	|	1	|
|	GB043	|	Is there productive morphological dual marking on nouns?	|	1	|
|	GB044	|	Is there productive morphological plural marking on nouns?	|	1	|
|	GB070	|	Are there morphological cases for non-pronominal core arguments (i.e. S/A/P)?	|	0	|
|	GB071	|	Are there morphological cases for pronominal core arguments (i.e. S/A/P)?	|	0	|
|	GB072	|	Are there morphological cases for oblique non-pronominal NPs (i.e. not S/A/P)?	|	0	|
|	GB073	|	Are there morphological cases for independent oblique personal pronominal arguments (i.e. not S/A/P)?	|	0	|
|	GB089	|	Can the S argument be indexed by a suffix/enclitic on the verb in the simple main clause?	|	1	|
|	GB090	|	Can the S argument be indexed by a prefix/proclitic on the verb in the simple main clause?	|	1	|
|	GB091	|	Can the A argument be indexed by a suffix/enclitic on the verb in the simple main clause?	|	1	|
|	GB092	|	Can the A argument be indexed by a prefix/proclitic on the verb in the simple main clause?	|	1	|
|	GB093	|	Can the P argument be indexed by a suffix/enclitic on the verb in the simple main clause?	|	1	|
|	GB094	|	Can the P argument be indexed by a prefix/proclitic on the verb in the simple main clause?	|	1	|
|	GB099	|	Can verb stems alter according to the person of a core participant?	|	1	|
|	GB109	|	Is there verb suppletion for participant number?	|	1	|
|	GB114	|	Is there a phonologically bound reflexive marker on the verb?	|	1	|
|	GB115	|	Is there a phonologically bound reciprocal marker on the verb?	|	1	|
|	GB165	|	Is there productive morphological trial marking on nouns?	|	1	|
|	GB166	|	Is there productive morphological paucal marking on nouns?	|	1	|
|	GB170	|	Can an adnominal property word agree with the noun in gender/noun class?	|	0	|
|	GB171	|	Can an adnominal demonstrative agree with the noun in gender/noun class?	|	0	|
|	GB172	|	Can an article agree with the noun in gender/noun class?	|	0	|
|	GB177	|	Can the verb carry a marker of animacy of argument, unrelated to any gender/noun class of the argument visible in the NP domain?	|	1	|
|	GB184	|	Can an adnominal property word agree with the noun in number?	|	0	|
|	GB185	|	Can an adnominal demonstrative agree with the noun in number?	|	0	|
|	GB186	|	Can an article agree with the noun in number?	|	0	|
|	GB198	|	Can an adnominal numeral agree with the noun in gender/noun class?	|	0	|
|	GB408	|	Is there any accusative alignment of flagging?	|	0	|
|	GB409	|	Is there any ergative alignment of flagging?	|	0	|
|	GB410	|	Is there any neutral alignment of flagging?	|	0	|
|	GB430	|	Can adnominal possession be marked by a prefix on the possessor?	|	0	|
|	GB431	|	Can adnominal possession be marked by a prefix on the possessed noun?	|	1	|
|	GB432	|	Can adnominal possession be marked by a suffix on the possessor?	|	0	|
|	GB433	|	Can adnominal possession be marked by a suffix on the possessed noun?	|	1	|
Table 1: Grambank features making up the locus of marking metric.

# Fusion
The degree to which a language encodes meanings and functions with bound morphology as opposed to phonologically free-standing markers (Bickel & Nichols 2007). At earlier stages of our project, this metric was known as "Boundness" or "Boundedness", which is why those terms sometimes also occur (the ParameterTable column name is "Boundness").

|	ID	|	Name	|	Fusion	|
|--	|--	|	--	|
|	GB042	|	Is there productive overt morphological singular marking on nouns?	|	1	|
|	GB043	|	Is there productive morphological dual marking on nouns?	|	1	|
|	GB044	|	Is there productive morphological plural marking on nouns?	|	1	|
|	GB047	|	Is there a productive morphological pattern for deriving an action/state noun from a verb?	|	0.5	|
|	GB048	|	Is there a productive morphological pattern for deriving an agent noun from a verb?	|	0.5	|
|	GB049	|	Is there a productive morphological pattern for deriving an object noun from a verb?	|	0.5	|
|	GB070	|	Are there morphological cases for non-pronominal core arguments (i.e. S/A/P)?	|	1	|
|	GB071	|	Are there morphological cases for pronominal core arguments (i.e. S/A/P)?	|	0.5	|
|	GB072	|	Are there morphological cases for oblique non-pronominal NPs (i.e. not S/A/P)?	|	1	|
|	GB073	|	Are there morphological cases for independent oblique personal pronominal arguments (i.e. not S/A/P)?	|	0.5	|
|	GB074	|	Are there prepositions?	|	0	|
|	GB075	|	Are there postpositions?	|	0	|
|	GB079	|	Do verbs have prefixes/proclitics, other than those that only mark A, S or P (do include portmanteau: A & S + TAM)?	|	1	|
|	GB080	|	Do verbs have suffixes/enclitics, other than those that only mark A, S or P (do include portmanteau: A & S + TAM)?	|	1	|
|	GB081	|	Is there productive infixation in verbs?	|	1	|
|	GB082	|	Is there overt morphological marking of present tense on verbs?	|	1	|
|	GB083	|	Is there overt morphological marking on the verb dedicated to past tense?	|	1	|
|	GB084	|	Is there overt morphological marking on the verb dedicated to future tense?	|	1	|
|	GB086	|	Is a morphological distinction between perfective and imperfective aspect available on verbs?	|	1	|
|	GB089	|	Can the S argument be indexed by a suffix/enclitic on the verb in the simple main clause?	|	1	|
|	GB090	|	Can the S argument be indexed by a prefix/proclitic on the verb in the simple main clause?	|	1	|
|	GB091	|	Can the A argument be indexed by a suffix/enclitic on the verb in the simple main clause?	|	1	|
|	GB092	|	Can the A argument be indexed by a prefix/proclitic on the verb in the simple main clause?	|	1	|
|	GB093	|	Can the P argument be indexed by a suffix/enclitic on the verb in the simple main clause?	|	1	|
|	GB094	|	Can the P argument be indexed by a prefix/proclitic on the verb in the simple main clause?	|	1	|
|	GB103	|	Is there a benefactive applicative marker on the verb (including indexing)?	|	1	|
|	GB104	|	Is there an instrumental applicative marker on the verb (including indexing)?	|	1	|
|	GB107	|	Can standard negation be marked by an affix, clitic or modification of the verb?	|	1	|
|	GB108	|	Is there directional or locative morphological marking on verbs?	|	1	|
|	GB113	|	Are there verbal affixes or clitics that turn intransitive verbs into transitive ones?	|	1	|
|	GB114	|	Is there a phonologically bound reflexive marker on the verb?	|	1	|
|	GB115	|	Is there a phonologically bound reciprocal marker on the verb?	|	1	|
|	GB119	|	Can mood be marked by an inflecting word ("auxiliary verb")?	|	1	|
|	GB120	|	Can aspect be marked by an inflecting word ("auxiliary verb")?	|	1	|
|	GB121	|	Can tense be marked by an inflecting word ("auxiliary verb")?	|	1	|
|	GB146	|	Is there a morpho-syntactic distinction between predicates expressing controlled versus uncontrolled events or states?	|	0.5	|
|	GB147	|	Is there a morphological passive marked on the lexical verb?	|	1	|
|	GB148	|	Is there a morphological antipassive marked on the lexical verb?	|	1	|
|	GB149	|	Is there a morphologically marked inverse on verbs?	|	1	|
|	GB151	|	Is there an overt verb marker dedicated to signalling coreference or noncoreference between the subject of one clause and an argument of an adjacent clause ("switch reference")?	|	1	|
|	GB152	|	Is there a morphologically marked distinction between simultaneous and sequential clauses?	|	1	|
|	GB155	|	Are causatives formed by affixes or clitics on verbs?	|	1	|
|	GB165	|	Is there productive morphological trial marking on nouns?	|	1	|
|	GB166	|	Is there productive morphological paucal marking on nouns?	|	1	|
|	GB170	|	Can an adnominal property word agree with the noun in gender/noun class?	|	1	|
|	GB171	|	Can an adnominal demonstrative agree with the noun in gender/noun class?	|	1	|
|	GB172	|	Can an article agree with the noun in gender/noun class?	|	1	|
|	GB177	|	Can the verb carry a marker of animacy of argument, unrelated to any gender/noun class of the argument visible in the NP domain?	|	1	|
|	GB184	|	Can an adnominal property word agree with the noun in number?	|	1	|
|	GB185	|	Can an adnominal demonstrative agree with the noun in number?	|	1	|
|	GB186	|	Can an article agree with the noun in number?	|	1	|
|	GB187	|	Is there any productive diminutive marking on the noun (exclude marking by system of nominal classification only)?	|	1	|
|	GB188	|	Is there any productive augmentative marking on the noun (exclude marking by system of nominal classification only)?	|	1	|
|	GB198	|	Can an adnominal numeral agree with the noun in gender/noun class?	|	1	|
|	GB262	|	Is there a clause-initial polar interrogative particle?	|	0	|
|	GB263	|	Is there a clause-final polar interrogative particle?	|	0	|
|	GB264	|	Is there a polar interrogative particle that most commonly occurs neither clause-initially nor clause-finally?	|	0	|
|	GB275	|	Is there a bound comparative degree marker on the property word in a comparative construction?	|	1	|
|	GB285	|	Can polar interrogation be marked by a question particle and verbal morphology?	|	1	|
|	GB286	|	Can polar interrogation be indicated by overt verbal morphology only?	|	1	|
|	GB298	|	Can standard negation be marked by an inflecting word ("auxiliary verb")?	|	1	|
|	GB299	|	Can standard negation be marked by a non-inflecting word ("auxiliary particle")?	|	0	|
|	GB302	|	Is there a phonologically free passive marker ("particle" or "auxiliary")?	|	0	|
|	GB303	|	Is there a phonologically free antipassive marker ("particle" or "auxiliary")?	|	0	|
|	GB312	|	Is there overt morphological marking on the verb dedicated to mood?	|	1	|
|	GB316	|	Is singular number regularly marked in the noun phrase by a dedicated phonologically free element?	|	0	|
|	GB317	|	Is dual number regularly marked in the noun phrase by a dedicated phonologically free element?	|	0	|
|	GB318	|	Is plural number regularly marked in the noun phrase by a dedicated phonologically free element?	|	0	|
|	GB319	|	Is trial number regularly marked in the noun phrase by a dedicated phonologically free element?	|	0	|
|	GB320	|	Is paucal number regularly marked in the noun phrase by a dedicated phonologically free element?	|	0	|
|	GB430	|	Can adnominal possession be marked by a prefix on the possessor?	|	1	|
|	GB431	|	Can adnominal possession be marked by a prefix on the possessed noun?	|	1	|
|	GB432	|	Can adnominal possession be marked by a suffix on the possessor?	|	1	|
|	GB433	|	Can adnominal possession be marked by a suffix on the possessed noun?	|	1	|
|	GB519	|	Can mood be marked by a non-inflecting word ("auxiliary particle")?	|	0	|
|	GB520	|	Can aspect be marked by a non-inflecting word ("auxiliary particle")?	|	0	|
|	GB521	|	Can tense be marked by a non-inflecting word ("auxiliary particle")?	|	0	|



## Variation in calculation of Fusion score
For the Fusion metric, Grambank features are classified into 0, 1 and 0.5 depending on wether they pertain to free-marking (0), bound marking (1) or a feature that maps onto bound marking - but also potentially other morphological patterns (clitic, tone, suppletion etc) - 0.5. When this metric was originally conceived we debated wether we should only count features that directly pertain to bound marking, or if we should also give "minus" values to languages that explicitly have free-standing marking. For the release paper (Skirgård et al 2023), we ended up using a version of the Fusion metric that only considers the 0.5 and 1 features. For a later paper, Shcherbakova et al (2023) we used a version of the score that only considers features with a Fusion value of 1. 

When writing [the R-package rgrambank](https://github.com/HedvigS/rgrambank/blob/main/README.md#functions), we decided to make three options available to users as an argument to the function `rgrambank::make_theo_scores()`:

* `count_zero_half_and_one` - features assigned as 0 will mean that the values for languages are reversed, i.e. free-marking with contribute _negatively_ to the fusion-score
* `count_one_only` - only consider features with a Fusion value of 1 (comparable to Shcherbakova et al 2023)
* `count_one_and_half` - consider only features with Fusion scores of 0.5 and 1 (comparable to Skirgår et al 2023)

The difference between `count_one_only` and `count_one_and_half` is minuscule [(the Pearson correlation between the two is 1)](https://github.com/HedvigS/rgrambank/blob/main/README.md#differences-in-calculation-of-fusion-score
). `count_one_and_half` is the default option for the function `rgrambank::make_theo_scores()`.

# Flexivity
Degree of allomorphic variation (Bickel & Nichols 2007). A high score for the flexivity metric indicates that a language has lexically conditioned allomorphy in multiple grammatical or lexical categories (e.g., noun classes and suppletion in lexical forms).

|	ID	|	Name	|	Flexivity	|
|--	|--	|	--	|
|	GB030	|	Is there a gender distinction in independent 3rd person pronouns?	|	1	|
|	GB038	|	Are there demonstrative classifiers?	|	1	|
|	GB039	|	Is there nonphonological allomorphy of noun number markers?	|	1	|
|	GB041	|	Are there several nouns (more than three) which are suppletive for number?	|	1	|
|	GB051	|	Is there a gender/noun class system where sex is a factor in class assignment?	|	1	|
|	GB052	|	Is there a gender/noun class system where shape is a factor in class assignment?	|	1	|
|	GB053	|	Is there a gender/noun class system where animacy is a factor in class assignment?	|	1	|
|	GB054	|	Is there a gender/noun class system where plant status is a factor in class assignment?	|	1	|
|	GB057	|	Are there numeral classifiers?	|	1	|
|	GB058	|	Are there possessive classifiers?	|	1	|
|	GB095	|	Are variations in marking strategies of core participants based on TAM distinctions?	|	1	|
|	GB096	|	Are variations in marking strategies of core participants based on verb classes?	|	1	|
|	GB098	|	Are variations in marking strategies of core participants based on person distinctions?	|	1	|
|	GB099	|	Can verb stems alter according to the person of a core participant?	|	1	|
|	GB109	|	Is there verb suppletion for participant number?	|	1	|
|	GB110	|	Is there verb suppletion for tense or aspect?	|	1	|
|	GB111	|	Are there conjugation classes?	|	1	|
|	GB116	|	Do verbs classify the shape, size or consistency of absolutive arguments by means of incorporated nouns, verbal affixes or suppletive verb stems?	|	1	|
|	GB170	|	Can an adnominal property word agree with the noun in gender/noun class?	|	1	|
|	GB171	|	Can an adnominal demonstrative agree with the noun in gender/noun class?	|	1	|
|	GB172	|	Can an article agree with the noun in gender/noun class?	|	1	|
|	GB177	|	Can the verb carry a marker of animacy of argument, unrelated to any gender/noun class of the argument visible in the NP domain?	|	1	|
|	GB187	|	Is there any productive diminutive marking on the noun (exclude marking by system of nominal classification only)?	|	1	|
|	GB188	|	Is there any productive augmentative marking on the noun (exclude marking by system of nominal classification only)?	|	1	|
|	GB192	|	Is there a gender system where a noun's phonological properties are a factor in class assignment?	|	1	|
|	GB198	|	Can an adnominal numeral agree with the noun in gender/noun class?	|	1	|
|	GB300	|	Does the verb for 'give' have suppletive verb forms?	|	1	|
|	GB321	|	Is there a large class of nouns whose gender/noun class is not phonologically or semantically predictable?	|	1	|
|	GB402	|	Does the verb for 'see' have suppletive verb forms?	|	1	|
|	GB403	|	Does the verb for 'come' have suppletive verb forms?	|	1	|



# Noun class/gender 
The noun class/gender metric allows us to assess the degree to which any latent pattern we observe is driven by flexivity in general versus the more specific phenomenon of noun class/gender, which makes up a large proportion of the features that contribute to the flexivity score.

|	ID	|	Name	|	Gender_or_Noun_Class	|
|--	|--	|	--	|
|	GB038	|	Are there demonstrative classifiers?	|	0	|
|	GB057	|	Are there numeral classifiers?	|	0	|
|	GB058	|	Are there possessive classifiers?	|	0	|
|	GB030	|	Is there a gender distinction in independent 3rd person pronouns?	|	1	|
|	GB051	|	Is there a gender/noun class system where sex is a factor in class assignment?	|	1	|
|	GB052	|	Is there a gender/noun class system where shape is a factor in class assignment?	|	1	|
|	GB053	|	Is there a gender/noun class system where animacy is a factor in class assignment?	|	1	|
|	GB054	|	Is there a gender/noun class system where plant status is a factor in class assignment?	|	1	|
|	GB170	|	Can an adnominal property word agree with the noun in gender/noun class?	|	1	|
|	GB171	|	Can an adnominal demonstrative agree with the noun in gender/noun class?	|	1	|
|	GB172	|	Can an article agree with the noun in gender/noun class?	|	1	|
|	GB177	|	Can the verb carry a marker of animacy of argument, unrelated to any gender/noun class of the argument visible in the NP domain?	|	1	|
|	GB192	|	Is there a gender system where a noun's phonological properties are a factor in class assignment?	|	1	|
|	GB196	|	Is there a male/female distinction in 2nd person independent pronouns?	|	1	|
|	GB197	|	Is there a male/female distinction in 1st person independent pronouns?	|	1	|
|	GB198	|	Can an adnominal numeral agree with the noun in gender/noun class?	|	1	|
|	GB321	|	Is there a large class of nouns whose gender/noun class is not phonologically or semantically predictable?	|	1	|


# Informativity
The Informativity metric is the degree to which basic grammatical meanings/functions are obligatorily encoded in the grammar (regardless of how, exactly, these meanings are encoded). This captures how much information needs to be specified when making an utterance in a language. For example, does the language have a rule that tense needs to be marked (regardless of how it is marked)? The informativity score allows us to ascertain whether our fusion metric is actually capturing a more general tendency for languages to require more types of information to be obligatorily encoded in grammar. The informativity score was computed in a different way compared to the other metrics. It was calculated by grouping features that pertain to the same grammatical function (reflexive, passive voice, singular number, etc.) and counting that function as present if a language has a positive value for any member of that set. An average was then taken across all available sets for a language, indicating how many of these functions are expressed, by either bound marking or free marking. A language with a low score for this index encodes fewer types of information obligatorily in grammar and may express these meanings optionally or lexically. A language with a high informativity score requires nonoptional expression of many different grammatical functions.

Noteworthy for this metric is that it is necessary to flip the values of GB140 to compute correctly.


|	ID	|	Name	|	Informativity	|
|--	|--	|	--	|
|	GB059	|	Is the adnominal possessive construction different for alienable and inalienable nouns?	|	alienability	|
|	GB148	|	Is there a morphological antipassive marked on the lexical verb?	|	antipassive	|
|	GB303	|	Is there a phonologically free antipassive marker ("particle" or "auxiliary")?	|	antipassive	|
|	GB086	|	Is a morphological distinction between perfective and imperfective aspect available on verbs?	|	aspect	|
|	GB120	|	Can aspect be marked by an inflecting word ("auxiliary verb")?	|	aspect	|
|	GB520	|	Can aspect be marked by a non-inflecting word ("auxiliary particle")?	|	aspect	|
|	GB046	|	Is there an associative plural marker for nouns?	|	assocplural	|
|	GB188	|	Is there any productive augmentative marking on the noun (exclude marking by system of nominal classification only)?	|	augmentative	|
|	GB314	|	Can augmentative meaning be expressed productively by a shift of gender/noun class?	|	augmentative	|
|	GB103	|	Is there a benefactive applicative marker on the verb (including indexing)?	|	benefactive	|
|	GB028	|	Is there a distinction between inclusive and exclusive?	|	clusivity	|
|	GB027	|	Are nominal conjunction and comitative expressed by different elements?	|	comitative	|
|	GB146	|	Is there a morpho-syntactic distinction between predicates expressing controlled versus uncontrolled events or states?	|	control	|
|	GB117	|	Is there a copula for predicate nominals?	|	copulaprednom	|
|	GB325	|	Is there a count/mass distinction in interrogative quantifiers?	|	count_mass	|
|	GB020	|	Are there definite or specific articles?	|	definitearticles	|
|	GB035	|	Are there three or more distance contrasts in demonstratives?	|	demonstartivedistance	|
|	GB038	|	Are there demonstrative classifiers?	|	demonstrative classifiers	|
|	GB036	|	Do demonstratives show an elevation distinction?	|	demonstrativeelevation	|
|	GB037	|	Do demonstratives show a visible-nonvisible distinction?	|	demonstrativevisibility	|
|	GB140	|	Is verbal predication marked by the same negator as all of the following types of predication: locational, existential and nominal?	|	differentneg	|
|	GB187	|	Is there any productive diminutive marking on the noun (exclude marking by system of nominal classification only)?	|	diminutive	|
|	GB315	|	Can diminutive meaning be expressed productively by a shift of gender/noun class?	|	diminutive	|
|	GB108	|	Is there directional or locative morphological marking on verbs?	|	directional	|
|	GB043	|	Is there productive morphological dual marking on nouns?	|	dual	|
|	GB317	|	Is dual number regularly marked in the noun phrase by a dedicated phonologically free element?	|	dual	|
|	GB322	|	Is there grammatical marking of direct evidence (perceived with the senses)?	|	evidentiality_direct	|
|	GB323	|	Is there grammatical marking of indirect evidence (hearsay, inference, etc.)?	|	evidentiality_indirect	|
|	GB126	|	Is there an existential verb?	|	existentialverb	|
|	GB053	|	Is there a gender/noun class system where animacy is a factor in class assignment?	|	genderanimacy	|
|	GB054	|	Is there a gender/noun class system where plant status is a factor in class assignment?	|	genderplant	|
|	GB051	|	Is there a gender/noun class system where sex is a factor in class assignment?	|	gendersex	|
|	GB052	|	Is there a gender/noun class system where shape is a factor in class assignment?	|	gendershape	|
|	GB021	|	Do indefinite nominals commonly have indefinite articles?	|	indef	|
|	GB104	|	Is there an instrumental applicative marker on the verb (including indexing)?	|	instrumental	|
|	GB149	|	Is there a morphologically marked inverse on verbs?	|	inverse	|
|	GB119	|	Can mood be marked by an inflecting word ("auxiliary verb")?	|	mood	|
|	GB312	|	Is there overt morphological marking on the verb dedicated to mood?	|	mood	|
|	GB519	|	Can mood be marked by a non-inflecting word ("auxiliary particle")?	|	mood	|
|	GB309	|	Are there multiple past or multiple future tenses, distinguishing distance from Time of Reference?	|	multipletense	|
|	GB057	|	Are there numeral classifiers?	|	numera classifers	|
|	GB147	|	Is there a morphological passive marked on the lexical verb?	|	passive	|
|	GB302	|	Is there a phonologically free passive marker ("particle" or "auxiliary")?	|	passive	|
|	GB166	|	Is there productive morphological paucal marking on nouns?	|	paucal	|
|	GB320	|	Is paucal number regularly marked in the noun phrase by a dedicated phonologically free element?	|	paucal	|
|	GB044	|	Is there productive morphological plural marking on nouns?	|	plural	|
|	GB318	|	Is plural number regularly marked in the noun phrase by a dedicated phonologically free element?	|	plural	|
|	GB415	|	Is there a politeness distinction in 2nd person forms?	|	politeness	|
|	GB058	|	Are there possessive classifiers?	|	possessive classifiers	|
|	GB127	|	Are different posture verbs used obligatorily depending on an inanimate locatum's shape or position (e.g. 'to lie' vs. 'to stand')?	|	postureverbs	|
|	GB139	|	Is there a difference between imperative (prohibitive) and declarative negation constructions?	|	prohibitive	|
|	GB031	|	Is there a dual or unit augmented form (in addition to plural or augmented) for all person categories in the pronoun system?	|	pronoundualaug	|
|	GB197	|	Is there a male/female distinction in 1st person independent pronouns?	|	pronoungender1	|
|	GB196	|	Is there a male/female distinction in 2nd person independent pronouns?	|	pronoungender2	|
|	GB030	|	Is there a gender distinction in independent 3rd person pronouns?	|	pronoungender3	|
|	GB167	|	Is there a logophoric pronoun?	|	pronounlog	|
|	GB115	|	Is there a phonologically bound reciprocal marker on the verb?	|	reciprocity	|
|	GB306	|	Is there a phonologically independent non-bipartite reciprocal pronoun?	|	reciprocity	|
|	GB114	|	Is there a phonologically bound reflexive marker on the verb?	|	reflexivity	|
|	GB305	|	Is there a phonologically independent reflexive pronoun?	|	reflexivity	|
|	GB152	|	Is there a morphologically marked distinction between simultaneous and sequential clauses?	|	simultanseq	|
|	GB042	|	Is there productive overt morphological singular marking on nouns?	|	singular	|
|	GB316	|	Is singular number regularly marked in the noun phrase by a dedicated phonologically free element?	|	singular	|
|	GB151	|	Is there an overt verb marker dedicated to signalling coreference or noncoreference between the subject of one clause and an argument of an adjacent clause ("switch reference")?	|	switch reference	|
|	GB082	|	Is there overt morphological marking of present tense on verbs?	|	tense	|
|	GB083	|	Is there overt morphological marking on the verb dedicated to past tense?	|	tense	|
|	GB084	|	Is there overt morphological marking on the verb dedicated to future tense?	|	tense	|
|	GB121	|	Can tense be marked by an inflecting word ("auxiliary verb")?	|	tense	|
|	GB521	|	Can tense be marked by a non-inflecting word ("auxiliary particle")?	|	tense	|
|	GB165	|	Is there productive morphological trial marking on nouns?	|	trial	|
|	GB319	|	Is trial number regularly marked in the noun phrase by a dedicated phonologically free element?	|	trial	|
|	GB177	|	Can the verb carry a marker of animacy of argument, unrelated to any gender/noun class of the argument visible in the NP domain?	|	verb_animacy	|
|	GB116	|	Do verbs classify the shape, size or consistency of absolutive arguments by means of incorporated nouns, verbal affixes or suppletive verb stems?	|	verbclassify	|


# References
* Skirgård, Hedvig, Hannah J. Haynie, Damián E. Blasi, Harald Hammarström, Jeremy Collins, Jay J. Latarche, Jakob Lesage, Tobias Weber, Alena Witzlack-Makarevich, Sam Passmore, Angela Chira, Luke Maurits, Russell Dinnage, Michael Dunn, Ger Reesink, Ruth Singer, Claire Bowern, Patience Epps, Jane Hill, Outi Vesakoski, Martine Robbeets, Noor Karolin Abbas, Daniel Auer, Nancy A. Bakker, Giulia Barbos, Robert D. Borges, Swintha Danielsen, Luise Dorenbusch, Ella Dorn, John Elliott, Giada Falcone, Jana Fischer, Yustinus Ghanggo Ate, Hannah Gibson, Hans-Philipp Göbel, Jemima A. Goodall, Victoria Gruner, Andrew Harvey, Rebekah Hayes, Leonard Heer, Roberto E. Herrera Miranda, Nataliia Hübler, Biu Huntington-Rainey, Jessica K. Ivani, Marilen Johns, Erika Just, Eri Kashima, Carolina Kipf, Janina V. Klingenberg, Nikita König, Aikaterina Koti, Richard G. A. Kowalik, Olga Krasnoukhova, Nora L.M. Lindvall, Mandy Lorenzen, Hannah Lutzenberger, Tônia R.A. Martins, Celia Mata German, Suzanne van der Meer, Jaime Montoya Samamé, Michael Müller, Saliha Muradoglu, Kelsey Neely, Johanna Nickel, Miina Norvik, Cheryl Akinyi Oluoch, Jesse Peacock, India O.C. Pearey, Naomi Peck, Stephanie Petit, Sören Pieper, Mariana Poblete, Daniel Prestipino, Linda Raabe, Amna Raja, Janis Reimringer, Sydney C. Rey, Julia Rizaew, Eloisa Ruppert, Kim K. Salmon, Jill Sammet, Rhiannon Schembri, Lars Schlabbach, Frederick W.P. Schmidt, Amalia Skilton, Wikaliler Daniel Smith, Hilário de Sousa, Kristin Sverredal, Daniel Valle, Javier Vera, Judith Voß, Tim Witte, Henry Wu, Stephanie Yam, Jingting Ye 葉婧婷, Maisie Yong, Tessa Yuditha, Roberto Zariquiey, Robert Forkel, Nicholas Evans, Stephen C. Levinson, Martin Haspelmath, Simon J. Greenhill, Quentin D. Atkinson & Russell D. Gray (2023) Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. Science Advances, 9(16), eadg6175. https://www.science.org/doi/10.1126/sciadv.adg6175

* Greenberg, J. H. (1963) Some universals of grammar with particular reference to the order of meaningful elements, in Universals of Language, J. H. Greenberg, Ed. MIT Press, pp. 73–113.

* Dryer, M. S. (1992). The Greenbergian word order correlations. Language, 68(1), 81-138.

* Nichols, J. (1986). Head-marking and dependent-marking grammar. Language, 62(1), 56-119.

* Bickel, B., & Nichols, J. (2007). Inflectional morphology. In T. Shopen (Ed.), Language typology and syntactic description: Volume 3: Grammatical categories and the lexicon (pp. 169-240). Cambridge University Press.

* Shcherbakova, O., Michaelis, S. M., Haynie, H. J., Passmore, S., Gast, V., Gray, R. D.,Greenhill, S.J., Blasi, D.E, & Skirgård, H. (2023). Societies of strangers do not speak less complex languages. Science advances, 9(33), eadf7704.


Author: Hedvig Skirgård