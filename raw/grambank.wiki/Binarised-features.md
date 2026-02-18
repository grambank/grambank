The Grambank questionnaire contains six features that are not binary but multistate. They are as follows:

ID | Name
-- | --
GB024 | What is the order of numeral and noun in the NP?
GB025 | What is the order of adnominal demonstrative and noun?
GB065 | What is the pragmatically unmarked order of adnominal possessor noun and possessed noun?
GB130 | What is the pragmatically unmarked order of S and V in intransitive clauses?
GB193 | What is the order of adnominal property word and noun?
GB203 | What is the order of the adnominal collective universal quantifier ('all') and the noun?

This can be undesirable for certain kinds of analysis, for example Gower-distances or dimensionality reduction techniques like PCA or MCA.

These multistate can be binarised by turning each into two features, "Is the order XY?" and "Is the order YX?". Importantly, in instances where the multi-state feature had been answered "both", this would trigger "1 (yes)" for _both_ binarised features. 

## The binarised versions of the multistate features
ID | Name
-- | --
GB024a | Is the order of the numeral and noun Num-N?
GB024b | Is the order of the numeral and noun N-Num?
GB025a | Is the order of the adnominal demonstrative and noun Dem-N?
GB025b | Is the order of the adnominal demonstrative and noun N-Dem?
GB065a | Is the pragmatically unmarked order of adnominal possessor noun and possessed noun PSR-PSD?
GB065b | Is the pragmatically unmarked order of adnominal possessor noun and possessed noun PSD-PSR?
GB130a | Is the pragmatically unmarked order of S and V in intransitive clauses S-V?
GB130b | Is the pragmatically unmarked order of S and V in intransitive clauses V-S?
GB193a | Is the order of the adnominal property word (ANM) and noun ANM-N?
GB193b | Is the order of the adnominal property word (ANM) and noun N-ANM?
GB203a | Is the order of the adnominal collective universal quantifier (UQ) and noun UQ-N?
GB203b | Is the order of the adnominal collective universal quantifier (UQ) and noun N-QU?

## How to do this in R
For the [Grambank release paper](https://github.com/grambank/grambank/wiki/Citing-grambank#release-paper), there is [a R-script in the github repos grambank-analysed that performs this action appropriately](https://github.com/grambank/grambank-analysed/blob/main/R_grambank/make_wide_binarized.R).

Since the release paper, we have constructed an R package for common actions such as this. You can use the function `make_binary_ValueTable` from [the R-package rgrambank](https://github.com/HedvigS/rgrambank/blob/main/README.md#functions) to compute binarised versions of the multistate features. Here is [an example script](https://github.com/HedvigS/rgrambank/blob/5e43183bb4fb62d9912b79f583e00b817b9e98c0/example_scripts/example_make_theo_scores.R#L19) showcasing the relevant functions. This action can also be performed on the Grambank ParameterTable with ` rgrambank::make_binary_ParameterTable()`.

## Changing how input coding is done
Since 2023-08 we have also updated [the underlying blank starter sheet ("Grambank_most_updated_sheet.tsv")](https://github.com/grambank/grambank/pull/46) - [new sheet here](https://github.com/grambank/grambank/blob/master/docs/Grambank_most_updated_sheet.tsv) - and [all existing coding sheets to also include explicitly](https://github.com/glottobank/Grambank/pull/2606
) separate lines for the binarised version of the multi-state features. We decided to give coders the binarised version of these features because this allows coding of "?" for one of the features, but not both. For example, if there is clear evidence for the order of numerals and nouns being Num-N but the situation is more unclear with N-Num it is possible to code the first one as "1 (yes)" and the second one as "?". When coders just had the multistate version before, this was less clear. Grambank version >2 have the binarised features, and also the multistate legacy coding (which can be binarised).

The binarised features that have been added to the coding questionnaire follow the same principle as the above-mentioned R-approach, with "a" and "b" being added onto the original multi-state feature parameter ID as shown below.

For the R-package [rgrambank](https://github.com/HedvigS/rgrambank/blob/main/README.md), we refer to Grambank coding that is binary already at the level of coder input as `native binary` to tell those data-points apart from coding that was multistate at input but which were then binarised when analysing. The function `rgrambank::make_binary_ValueTable` has the following related arguments to allow users full control of their analytical decisions. It is possible for example that a user does not want to mix `native binary` and binarised features but just wants one or the other.

* `keep_multistate` if `TRUE` keep datapoints of the multistate features alongside the native binary and/or binarised datapoints of the same multistate features (defaults to `FALSE`)
* `keep_native_binary` if there are native binary datapoints, keep those alongside the binarised datapoints (defaults to `TRUE`)
* `trim_to_only_native_binary` if `TRUE`, then multistate datapoints are dropped and they are also not binarised, only native binary datapoints are kept (defaults to `FALSE`)

## Why do this?
If you are calculating distances between languages using Grambank data, you most likely want a language coded as 1 for GB065 to be closer to a language coded as 3 than it is to a language coded as 2. Having a PSR-PSD (1) is closer to having both orders (3, PSR-PSD and PSD-PSR) than it is to "just" having PSD-PSR (2). This is an analytical decision that you need to make, but we just want to alert you to this situation in case it is relevant for you.

Similarly, if you are doing dimensionality reduction like PCA/MCA, you also want the values (e.g. 1, 2, 3, 4) of your variables to have the same kind of relationship to each other. PCA will even assume that they are numbers in a sensible order (e.g. 1, 2, 3 are on a scale with the same distance between each other 1 and 3 are double the distance of 1 and 2).

While most features in Grambank are binary and therefore alright in this capacity, we need to do transformations for the multistate features as outlined above. For example, there is GB065: "What is the pragmatically unmarked order of adnominal possessor noun and possessed noun?". This features has the values: 1 (Possessor-Possessed), 2 (Possessed-Possessor) or 3 (both). Value 3 here is "both 1 and 2", which means that languages of this value (3) has a different relationship to languages with the values 1 and 2 than for example languages of 1 has to 3. The distances between 1 and 2 is not the same "kind" of distances as between 1 and 3. This is no good for MCA and PCA, we can't have it this way. We got to binarise these features in order for them to be acceptable according to the assumptions of MCA and PCA. We need to turn GB065 into two binary features, one that asks "is the possessor before the possessed" and one that is "is the possessor after the possessed". Languages that are coded for 3 (both) should have a 1 value for both of these new binarised features. Once the Grambank features have been binarised in the fashion outlined above, we can proceed with further analysis.

### What not to do
It is important to follow the principle outlined above whereby the multistate features are turned into _two_ binary features. It is not a generally good idea to turn them into three with the third being of the kind "GB065c Is the pragmatically unmarked order of adnominal possessor noun and possessed noun PSR-PSD and PSD-PSR?". This once again makes languages with the value 3 unnecessarily dissimilar from 1 and 2.
