In the Grambank project there is an option for coders to write comments for each data point. This is highly encouraged, as it makes it easier later to understand how the coding came about. This is relevant both for future users of the database and the project itself as we re-evaluate older coding. Comments give people reasons for why you coded as you did and can make it possible to understand in case of disagreement, unusual features etc. There are a few guidelines when it comes to comments in Grambank coding.

* **More is good**. Make good comments often, even if something seems obvious to you. We strive for at least 25 features having comments in each coding sheet.
* **Absence of evidence, evidence of absence**. If something is coded "?" or "0" because it is not described at all, please note "Not mentioned" in the comment. See also [our article on absence of evidence](https://github.com/grambank/grambank/wiki/Absence-of-evidence).
* **Be professional**. Remember that everyone can read your comments. 
* **Don't use "I"**. More than one person may end up editing a data point, to make it easier please stick to describing the language situation in the comments and avoid "I think that...".
* **Don't write "as above"**. The features can be reordered in the database. This means that you should not refer to other features in the comments, for example, by commenting "see above". If you have the same comment about many features, copy-paste.
* **Delete "to do", "look up" etc**. The comments in the coding sheet when submitted should be the final version as they show up in the dataset. Any notes to yourself about the work should be removed. You can make a new column for comments to yourself to make this easier. Only `Value, Source, Comment` and `Contributed_datapoint` end up in the dataset, other columns are ignored so you are free to add on extra ones (unless it's a revision).
* **Ancient languages**. If you are coding ancient languages and the source mixes analysis of corpora with reconstructions based on other languages, mark data points in the second category with "Reconstruction" in the comment field.
* **Rare coding requires comments**. Certain coding is deemed rare and requires a comment. See exactly which [here](https://github.com/grambank/grambank/wiki/Automatic-quality-checks#describe-check-of-value-and-comment). Our pygrambank sanity checks will report an error if they do not have a comment but are coded "1".
* **Characters**. Use UTF-8 character encoding. The files are set to this by default, make sure that when you open in LibreOffice you specify "UTF-8" as well in the dialogue box after clicking the file. Avoid using the "low down" quotation marks („…“), they tend to end up as tofu-boxes (□). Avoid Microsoft Excel at all costs.

**When to comment?**
The question might actually be the reverse, when not to comment? More comments are essentially always better. The only time it is not necessary to comment is when the information is very obvious in the source and it would slow down the coder by typing down the circumstances of the coding decisions. Otherwise, feel free to leave as many and as long comments as you see necessary. 

It is especially relevant to comment:
* when you have to do any kind of advanced interpretation to get at the information
* when the author(s) are using terminology that differs from the terminology framework in grambank
* when you have derived information from examples rather than specific statements in the descriptions
* when the phenomenon is unusual regionally or globally
* if you code a 0 or ? because the information is not mentioned. In such cases, comment "Not mentioned".

**Guidelines**
When writing comments, be as clear and specific as possible. It is encouraged to specify the specific morpheme in question and detail both the author's terminology and how it relates to ours. Avoid first person personal pronouns, the data point may be re-evaluated by other coders along the way anyway. Don't be unprofessional, be neutral and clear in regards to the information you have found and what you ended up coding based on it. Run a spell-checking program on the column "Comment" before submitting to catch any typos. 

**Awaiting feedback from patron/node/expert***
Avoid comments like "will check with patron", "will check with author". If you are waiting for feedback from a patron, node meeting or expert then do one of these two things:

a) wait with submitting the sheet until the information arrives 
b) submit the sheet with ?-value and explain what the confusion concerns. Once feedback arrives, update.

If you feel the need to keep track of which features you are currently waiting for feedback on, add that information in a new column. Do not use the comment column for this. This rule exist because sometimes the data-point decision is resolved but the comment "will check" remains, and that makes it difficult for future users and coders.


For comment guidelines when revising existing coding, go [here](https://github.com/grambank/grambank/wiki/Revising-existing-coding#basics).
