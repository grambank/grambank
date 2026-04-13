Languages can have multiple strategies for encoding the same function. In such cases, the Grambank questionnaire allows us to code for multiple strategies present in a language, not just the one that is deemed dominant.

An example of this is the feature set on polar questions. Some languages may have different regular strategies for forming polar questions, including changing the intonation of a clause, adding a clause-final interrogative particle, or changing the tone of the final syllable of a clause. Such languages are coded 1 for GB257, for GB263 and GB291, even if one of the strategies is the dominant pattern. Note, all constructions need to be productive.

* GB257 [Can polar interrogation be marked by intonation only?](https://github.com/grambank/Grambank/wiki/GB257)
* GB260 [Can polar interrogation be indicated by a special word order?](https://github.com/grambank/Grambank/wiki/GB260)
* GB262 [Is there a clause-initial polar interrogative particle?](https://github.com/grambank/Grambank/wiki/GB262)
* GB263 [Is there a clause-final polar interrogative particle?](https://github.com/grambank/Grambank/wiki/GB263)
* GB264 [Is there a polar interrogative particle that most commonly occurs neither clause-initially nor clause-finally?](https://github.com/grambank/Grambank/wiki/GB264)
* GB285 [Can polar interrogation be marked by a question particle and verbal morphology?](https://github.com/grambank/Grambank/wiki/GB285)
* GB286 [Can polar interrogation be indicated by overt verbal morphology only?](https://github.com/grambank/Grambank/wiki/GB286)
* GB291 [Can polar interrogation be marked by tone?](https://github.com/grambank/Grambank/wiki/GB291)
* GB297 [Can polar interrogation be indicated by a V-not-V construction?](https://github.com/grambank/Grambank/wiki/GB297)

Similarly, some word order features are multi-valued and give the option to code that more than one word order is possible:

| Feature number | Feature name | Possible Values |
| --- | --- | --- |
| GB130 | What is the pragmatically unmarked order of S and V in intransitive clauses? | (1 = SV, 2 = VS, 3 = both) |
| GB056 | What is the pragmatically unmarked order of adnominal possessor noun and possessed noun? | (1 = possessor-possessed, 2 = possessed-possessee, 3 = both)

### Dialectal variation
If there is variation between dialects that result in different coding for a given feature, you should split that coding up into two separate sheets each assigned to a dialect-level glottocode. If you are unsure of what glottocodes to assign, raise an issue and we'll help you. In some cases, we make a request to Glottolog for revisions or additions of new dialect glottocodes if the current state is not satisfactory. 

We want to avoid coding a language and also a dialect of that language, we would rather want two dialect coding sheets of the same language.

Keep in mind that we want evidence for each data point as it relates to each languoid, i.e. there may be a lot of missing data for each dialect if the descriptions are spotty. That is okay.

### Author disagreements
If you encounter a situation where there are multiple authors who have described the same language and they disagree on the analysis of a language phenomenon we have some principles you should apply

1) Does the disagreement actually result in different coding in the Grambank questionnaire? They may be disagreeing on something that ends up having no relevance for our features.
2) Are they in fact describing two (or more) different dialects/sub-varieties? If so, we should encode these in two (or more) separate coding sheets. If Glottolog already has appropriate dialect glottocodes for the varieties, use those. If not, we can request from the Glottolog-editors that new dialect glottocodes are generated. Note that it would still be good to run through step (3) even if this is the case, always critically evaluate the content.
3) If they are in fact describing exactly the same variety and the disagreement does pertain to Grambank features, evaluate a) which description is the most internally consistent, in other words, use your critical thinking skills to judge which grammatical description is "the best". Examples of non-consistent descriptions are for example contradictions between examples and prose. The second principle to keep in mind is b) how the concepts in the descriptions map onto the definitions we use in this typological project. Which description aligns best with how we have defined the phenomena in question?
4) Lastly, if you are not able to determine what to do after completing these steps, bring it up for discussion at your next node meeting. It is possible that this is a complex language phenomena that isn't well-enough described for us to code, meaning we should code "?".

### Changes in progress
In cases where there is a variation that arises because of a change in progress, code for the older state.

### Borrowings

In some cases, one of the competing strategies is the result of recent borrowing. Where a strategy has been borrowed recently, and the borrowing process is unmistakable, we are only interested in the more archaic strategies. The recently borrowed strategies should be mentioned in the comments, but should not be coded. For the features on numeral systems, for example, any clearly borrowed numeral system should be ignored. This means that in Island Carib [Glottolog: isla1278], for instance, there is no evidence of a decimal numeral system (GB333) or a vigesimal numeral system (GB335): all numerals above 4 are expressed "by using the words of the French patois of the country" (Rat 1898: 300).

If a strategy has been borrowed in the distant past (usually pre-colonial times) or if it's not clear whether it has been borrowed, the strategy should still be coded in Grambank.

**References**

Joseph Numa Rat. 1898. The Carib Language as now spoken in Dominica, West Indies. *Journal of the Royal Anthropological Institute of Great Britain and Ireland* XXVII. 293-315.
