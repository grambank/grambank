# Overview

Several features in Grambank concern systems of nominal classification such as noun class/gender and classifiers. For example, [GB198](https://github.com/grambank/grambank/wiki/GB198) (Can an adnominal numeral agree with the noun in noun class/gender?) asks whether the numeral agrees with the noun class/gender of the noun, and [GB057](https://github.com/grambank/grambank/wiki/GB057) (Are there numeral classifiers?) asks whether there are numeral classifiers. Languages which answer 1 for either of these look similar, in that either type will have a morpheme used with the numeral that varies depending on the noun.

Japanese (ISO 639-3: jpn, Glottolog: nucl1643) has numeral classifiers (Haspelmath 2018:4). In the following example, _-biki_ is a numeral classifier, and _inu_ 'dog’ belongs to the class of nouns that _-biki_ is used with. Japanese has been coded 1 for GB057.

```
inu       san-biki
dog(BIKI) three-CL.BIKI
‘three dogs’
```

Compare the above example with the following example from Cicipu (ISO 639-3: awc, Glottolog: cici1237), where _kà-_ is the noun class prefix used with numerals that modify nouns such as _kà-bárá_ 'old man’ (McGill 2009:285-286). Cicipu has been coded 1 for GB198. 

```
kà-bárá      ká-mpà   kà-yápù
CL1-old.man  CL1-this CL1-two
‘these two old men’
```

These two phenomena look similar, but are described as numeral classifiers in the case of Japanese and as a gender system in the case of Cicipu, where the numeral can agree with the noun.

# Grambank’s General Procedure

Grambank utilizes the following criteria in distinguishing gender/noun classes from classifiers:
1. Is there a system of nominal classification where some markers vary based on the category of the noun?
2. If the relevant markers are used only or primarily with numerals, demonstratives and possessors (or some subset of those), this is not sufficient to count as gender marking. Consider whether these markers meet our criteria for numeral, demonstrative or possessive classifiers.
3. If these elements systematically co-occur with some other element in the noun phrase or with indexing on the predicate, they should be considered noun class/gender markers.
4. If there are nominal classification markers which do not systematically co-occur with other constituents in the noun phrase or with indexing, then consider whether these markers meet our criteria for classifiers.

## Types of Classifiers Included in Grambank


[Possessive Classifiers:](https://github.com/grambank/Grambank/wiki/GB058) 
A system of nominal classification in which classifiers appear only within possessive constructions and are not related to other nominal classification systems such as the gender/noun class of the language, numeral classifiers or demonstrative classifiers. 

[Numeral Classifiers:](https://github.com/grambank/Grambank/wiki/GB057)
A system of nominal classification in which cardinal numerals occur with markers that vary depending on the modified noun. These markers are not the same as markers of a gender system used also on noun modifiers other than cardinal numerals, demonstratives, possessives or on predicates. 

[Demonstrative Classifiers:](https://github.com/grambank/Grambank/wiki/GB038) 
A system of nominal classification in which demonstratives occur with markers to classify the noun. Demonstrative classifiers can have the same form as numeral, possessive or verbal classifiers. These markers are not the same as the markers of a gender system used also on noun modifiers other than cardinal numerals, demonstratives, possessives or on predicates. 

[Verbal Classifiers:](https://github.com/grambank/Grambank/wiki/GB116)
A system of nominal classification in which verbal classifiers appear on the verb and classify a noun. Incorporated nouns or suppletive verb stems are subtypes of verbal classifiers. Verbal classifiers can be identical or very similar to demonstrative classifier systems. These markers are not the same as the markers of a gender system.

# Other Information

The information below may help you distinguish between noun class/gender and classifiers but does not supersede Grambank’s working definition above for the purposes of feature coding.

## Haspelmath
Grambank’s criteria are inspired largely by Haspelmath's discussion of the problem of distinguishing classifiers from noun class/gender (2018).
Haspelmath (2018: 5) proposes that both classifiers and noun class markers are types of 'nomification'. A 'nomifier system' is a unified term that includes systems traditionally called 'gender' as well as those traditionally labeled 'classifiers', defined as "a paradigm of grammatical markers which occur on noun-associated forms and each of which reflects a broad property of the corresponding noun other than person and number".
Regarding the traditional notion of gender/noun class, Haspelmath argues that ‘nomification’ systems with up to 20 categories, whose grammatical markers are not restricted to occurring with specific elements that include numerals and possessors, can be considered as potential noun class/gender systems.

## Aikhenvald 
Aikhenvald (2006), on the other hand, proposes criteria that more or less distinguish noun class/gender systems from classifiers.
Her proposed criteria (2006: 4) for noun class/gender systems are:

1. "There is a limited, countable number of classes."
2. "Each noun in the language belongs to one (or sometimes more than one) class."
3. "There is always some semantic basis to the grouping of nouns into gender classes, but languages vary in how much semantic basis there is. This usually includes animacy, humanness and sex, and sometimes also shape and size."
4. "Some constituents outside the noun itself must agree in gender with a noun. Agreement can be with other words in the noun phrase (adjectives, numbers, demonstratives, articles, etc.) and/or with the predicate of the clause, or an adverb."

Noun classifiers are discussed along the following lines by Aikhenvald (2006: 9): 

1. "Noun classifiers categorize the noun with which they co-occur and are independent of any other element in a noun phrase or in a clause. They are often independent words with generic semantics. Thus, in Yidiny, an Australian language, one would not generally say: ‘the girl dug up the yam’; it is more felicitous to include generics and say ‘the person girl dug up the vegetable yam’."
2. "Every noun in a language does not necessarily take a noun classifier. And a noun may occur with more than one classifier." 

Regarding numeral classifiers, in particular, she proposes the following definition:

1. "Numeral classifiers are morphemes that only appear next to a numeral, or a quantifier; they may categorize the referent of a noun in terms of its animacy, shape, and other inherent properties."

Possessive classifiers are described by Aikhenvald (2006: 14) as follows:

1. "Relational classifiers categorize the ways in which noun referents relate to, or can be manipulated by, the possessor – whether they are to be eaten, drunk, worn, etc."
2. "Possessed classifiers characterize a possessed noun itself, based on the physical properties (shape, form, consistency, function) or animacy of its referent."
3. Possessor classifiers are conditioned by the properties of the possessor. 

# References

Aikhenvald, Alexandra Y. 2006. Classifiers and noun classes: semantics. In Keith Brown (ed.) *Encyclopedia of languages and linguistics*, 463-471. Oxford: Elsevier.

Haspelmath, Martin. 2018. Toward a new conceptual framework for comparing gender systems and some so-called classifier systems. Talk presented at Stockholm University, Department of Linguistics on April 13, 2018.

Seifart, Frank, and Doris L. Payne. "Nominal classification in the North West Amazon: Issues in areal diffusion and typological characterization." International Journal of American Linguistics 73.4 (2007): 381-387.

