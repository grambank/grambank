## Logical dependencies in Grambank

A logical dependency is a situation where the presence of one phenomenon necessarily predicts the presence of another. For example, we could define two features (a) and (b), where (a) encodes the presence of a noun class system (1 means that it is present; 0 means that it is absent), and (b) encodes whether there is a noun class for plants (1 means that such a feature exists; 0 means that it does not exist). If (a) is coded 0, then (b) is also necessarily coded 0: if there is no noun class system, there logically cannot be a noun class for plants. 

Logical dependencies limit the types of statistical analyses that can be applied to a dataset. For this reason, we try to avoid logical dependencies in Grambank. The Grambank questionnaire has inherited features from [a number of earlier questionnaires](https://github.com/grambank/grambank/wiki/Background-of-the-Grambank-questionnaire). Some of these questionnaires included logically dependent features. From a set of over 400 features from these other surveys, we pruned away logically dependent features. We then also added a number of new questions and finally we arrived at 195 features.

Four features concerning articles in our dataset are not fully independent of each other:

* GB020 [Are there definite or specific articles?](https://github.com/grambank/Grambank/wiki/GB020)
* GB021 [Do indefinite/non-specific nominals commonly have indefinite/non-specific articles?](https://github.com/grambank/Grambank/wiki/GB021)
* GB022 [Are there prenominal articles?](https://github.com/grambank/Grambank/wiki/GB022)
* GB023 [Are there postnominal articles?](https://github.com/grambank/Grambank/wiki/GB023)

In practice, a 'yes' for either GB022 and/or GB023 necessarily results in a 'yes' for either GB020 or GB021. If there are prenominal or postnominal articles, then there are also definite or indefinite articles. In theory, however, this depends on one's understanding what an 'indefinite article' is. A language could have an indefinite article that is not commonly used, one that is for example equivalent to the English existential quantifiers *any* or *some*. In this case, the indefinite article would trigger a 1 in GB022 or GB023, but not in GB022.

There are also two sets, outlined below, where it is impossible for a language to be coded as 0 for all features. It is not possible to have no word order whatsoever, and to not have at least one alignment system. For more on the specifics of this, visit the respective articles.

**Transitive verb-order set**
* [GB131 Is a pragmatically unmarked constituent order verb-initial for transitive clauses?](https://github.com/grambank/Grambank/wiki/GB131)
* [GB132 Is a pragmatically unmarked constituent order verb-medial for transitive clauses?](https://github.com/grambank/Grambank/wiki/GB132)
* [GB133 Is a pragmatically unmarked constituent order verb-final for transitive clauses?](https://github.com/grambank/Grambank/wiki/GB133)

**Alingment set**
* [GB408 Is there any accusative alignment of flagging?](https://github.com/grambank/Grambank/wiki/GB408)
* [GB409 Is there any ergative alignment of flagging?](https://github.com/grambank/Grambank/wiki/GB409)
* [GB410 Is there any neutral alignment of flagging?](https://github.com/grambank/Grambank/wiki/GB410)

## Logical dependencies between Grambank and other databases

At various stages in the project, we have tried to map logical dependencies between Grambank features, features in the [databases that precede Grambank](https://github.com/grambank/grambank/wiki/Background-of-the-Grambank-questionnaire), and other cross-linguistic databases.

To formalize the dependencies, we used a system of parentheses and logical symbols. Each feature is represented by its feature ID followed by colons and the values that trigger the dependency. The following other symbols were used:

* () = bracketing information
* and = and (all feature values need to be met)
* or = or (inclusive or, i.e. 'and/or')
* -> = implies that
* : = follows feature number and indicates the value of that feature that is involved in the dependency.

The following example can be read like this: 'if there is a value 0 in feature 83 and a value 0 in feature 84, feature 85 necessarily has value 0'.

(83:0 and 84:0) -> 85:0

Each dependency statement is directed, meaning that from the example above we _cannot_ assume that the following is also true 85:0 -> (83:0 and 84:0).

Furthermore, the *value* of each feature needs to be specified. From the example above we _cannot_ assume that the following is true: (83:1 and 84:1) -> 85:1

If we have two features where the value of feature 1 is always predictable from the value of feature 2, this means that the two features are entirely identical.

When mapping to other datasets, the feature ID also includes the necessary abbreviated name of the dataset, e.g.

[ARGEX5-1:1](http://sails.clld.org/parameters/ARGEX5-1#5/1.746/289.565) -> [GB070:1](http://grambank.clld.org/parameters/GB070)

There are also more complex relationships. For example a, a combination of values in four different features could predict the value of a fifth feature:

(GB030:1 and GB050:0 and GB197:0 and GB196:0) -> GB055:1

When writing more than one dependency relationship, we separate them with commas:

45:0 -> (205:na and 206:na), (205:1 or 206:1) -> 45:1

When writing down dependencies, it is important:
* to specify both directions if they're both logically relevant, i.e. XX001:1 ->XX002:1 and XX002:1 -> XX001:1
* to specify all values of a feature that are dependent, i.e. both  XX001:1 ->XX002:1 and  XX001:0 ->XX002:0
* to remember that 'or' is inclusive or ('and/or')
* to remember that 'and' means that all conditions within the scope need to be met


# Other dependencies in Grambank
Besides strict local dependencies between existing features in Grambank, it can be necessary to consider relationships between features as mediated by a currently non-existing feature. For example, Grambank contains several features which concern gender/noun classification. They do not logically depend on each other, but if one were to consider a new feature such as "Is there gender/noun class at all?" they would all be strictly depended on this. There are also non-logical dependencies that can be relevant for some research. For more on this, please read:

```
Graff, A., Chousou-Polydouri, N., Inman, D., Skirgård, H., Lischka, M., Zakharko, T., ... & Bickel, B. (2025). Curating global datasets of structural linguistic features for independence. Scientific data, 12(1), 106. [PDF](https://www.nature.com/articles/s41597-024-04319-4.pdf)
```

Some users may also want to consider other dependencies in the dataset such as functional ones. Please consider carefully how to treat the data for your individual research question. It may be that you want to use distances from dimension-reduction techniques (e.g. PCA, MDS), Grambank as pruned for dependencies according to Graff et al 2025) or other alternatives.