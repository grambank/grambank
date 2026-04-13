Due to data imports from other databases and rare mishaps, we sometimes have more than 1 coding sheet for one language. Most of the time, the different coding sheets agree on the same value for the same feature, but sometimes they don't - these called 'coding conflicts'. In order to better understand the coding process, we want to go through all conflicts and (a) classify them into different types of conflicts and (b) resolve them to the best of our abilities (i.e. decide which is the appropriate coding).

In order to do this, we have merged all sheets for the same languoid where there is at least 1 conflict into 1 sheet. In the merged sheet for each languoid, there is one row per unique value. That means that if there is a conflict, there is more than 1 row for one feature, see the example below for illustration. 

All rows with conflicts are marked by True in the Conflict column. Please disregard completely all rows with False in the conflict column.

Don't do resolution of conflicts for a language you coded, the person resolving should always be distinct from the persons coding originally.

### Columns
This conflict sheet has some new columns compared to regular Grambank language coding sheets which are relevant for the workflow. Below is a list of all columns in these merged sheets and a description.

* `Feature_ID`	- Feature ID as usual
* `Value`		- Value as usual
* `Conflict`	- This is set to True or False depending on whether the feature has conflicting values. Disregard any row with False.
* `Classification of conflict`	- This is to be filled in by the coder reviewing the conflicts from a set or pre-determined categories
* `Select` - This is to be filled in by the coder reviewing the conflicts. The value(s) that is the best coding received a "True" in this column.
* `Sheet`	- Specification of from which sheet the coding was taken
* `Source`	- Source as listed for this datapoint in the original coding sheet for that value
* `Contributed_Datapoint`	- Inherited from original sheets, but is also to be used by reviewing coder
* `Comment`	- Source as listed for this datapoint in the original coding sheet for that value
* `Warnings` - If this datapoint triggered any of our automatic quality checks, it would be indicated here. If so, take that into account when reviewing

### Example
For fiji1243 we have coding both inherited from the old Sahul-survey (as indicated by the coders being MD, GR and RSI) and more recent coding by our grambank coder RSC. For feature GB020, they disagree on the value. This is why the column `Conflict` is set to `True`. However, for GB021 they agree, which is why `Conflict` is `False`. Neither coding sheet for neither of the features have any comment, and the source happens to be the same, but the page numbers differ.

Feature_ID	|Value|	Conflict|	Classification of conflict	|Select|	Sheet	|Source	|Contributed_Datapoint	|Comment|	Warnings|
| ---- |  ---- |----------- |  ----------- |  ----------- |  ------ |  ------ |  ------ |  ------ |  ------ |  
GB020	|0|	True	|	|	|MD-GR-RSI_fiji1243	|Dixon 1988:114		|	
GB020	|1|	True	|	|	|RSC_fiji1243	|Dixon 1988:32, 35-36, 114-115	|	
GB021	|0|	False	|	|	|MD-GR-RSI_fiji1243|	Dixon 1988:114	|		
GB021	|0|	False	|	|	|RSC_fiji1243|	Dixon 1988:36	|

### Conflict resolution steps
1. Assign yourself to a languoid to review in to do-list
2. Find the relevant sources listed in the merged sheet
3. Evaluate if the sources are indeed describing the same variety, or if this is an instance where the coding sheets should be assigned to different dialect glottocodes
4. Review the coding conflict and determine what is the best coding. Follow the same principles as [revisions](https://github.com/grambank/grambank/wiki/Revising-existing-coding) for Git workflow, i.e.: don't move the file, don't reorder the file, make PR and tag reviewers.
5a. If the best coding is one that exists in the sheet, mark that as "True" in the select column, mark your initials in "Contributed_Datapoint"
5b. If the best coding is not one that is already in the sheet, make a new row, leave the column Sheet empty and mark that row as "True" in the column called select and finally mark your coder initials in `Contributed_Datapoint`. This could for example be the case where the conflicting values are `0` and `1`, but the situation is so unclear that a `?` value is warranted.
6. Determine the reason for the conflict. See list of pre-determined reasons below.
7. Make a PR. Do not move the sheet from `conflicts` to `conflicts_resolved`, keep it where it is.

### Reasons for conflicts

For each value that you determine is incorrect, you need to select a possible reason for the erroneous coding. For correct coding, just write "correct" in the column "classification of conflict".

* `correct` - this is the correct value for this datapoint
* `typo` - there is no apparent reason, given the source(s) and the comment the inaccurate coding appears to be a typo
* `overcautious`
* `overconfident`
* `feature interpretation` - the different coders have interpreted the feature differently (some perhaps coded outside of the project and weren't in the loop with the specifics)
* `source interpretation` - the  different coders have interpreted the source(s) differently
* `sources disagree`
* `new source was consulted in other coding`
* `missed` - some coders have missed a section in a source
* `less thorough coding` - the other coder(s) were particularly thorough and spotted something that could easily have been missed or contacted expert(s)
* `hard to code` - the language phenomena is difficult to neatly fit into the questionnaire and took considerable discussion to resolve
* `unclear` - it is not clear why there is a conflict

### Example of outcome (one, or more, coder is correct)

After reviewing the case, it is determined that the appropriate coding for GB020 for this language is indeed "1", like RSC had coded. The correct row is marked with `True` for `Select` and `Classification of conflict` and `Contributed_Datapoint` are also filled out appropriately. Optionally, `Comment` is also filled out.

Feature_ID	|Value|	Conflict|	Classification of conflict	|Select|	Sheet	|Source	|Contributed_Datapoint	|Comment|	Warnings|
| ---- |  ---- |----------- |  ----------- |  ----------- |  ------ |  ------ |  ------ |  ------ |  ------ |  
GB020	|0|	True	|feature interpretation	|	|MD-GR-RSI_fiji1243	|Dixon 1988:114		|
GB020	|1|	True	|	|	True |RSC_fiji1243	|Dixon 1988:32, 35-36, 114-115	| HS| The article 'na' qualifies as a specific article	
GB021	|0|	False	|	|	|MD-GR-RSI_fiji1243|	Dixon 1988:114	|		
GB021	|0|	False	|	|	|RSC_fiji1243|	Dixon 1988:36	|


### Example of outcome (neither coder is correct)

After reviewing the case, it is determined that the appropriate coding for GB020 for this language is "?", which none of the other coders had selected. A row is added, with "?" as `Value` and is marked with `True` for `Select` and `Contributed_Datapoint` are also filled out.  `Classification of conflict` is filled out. Optionally, `Comment` is also filled out.

Feature_ID	|Value|	Conflict|	Classification of conflict	|Select|	Sheet	|Source	|Contributed_Datapoint	|Comment|	Warnings|
| ---- |  ---- |----------- |  ----------- |  ----------- |  ------ |  ------ |  ------ |  ------ |  ------ |  
GB020	|0|	True	|feature interpretation	|	|MD-GR-RSI_fiji1243	|Dixon 1988:114		|	
GB020	|1|	True	|feature interpretation	|	|RSC_fiji1243	|Dixon 1988:32, 35-36, 114-115	|	
GB020	|?|	True	|		|	True |	|Dixon 1988:32, 35-36, 114-115	|	HS| It is not clear from the grammar what the exact semantics is of 'na'
GB021	|0|	False	|	|	|MD-GR-RSI_fiji1243|	Dixon 1988:114	|		
GB021	|0|	False	|	|	|RSC_fiji1243|	Dixon 1988:36	|

### Adding content to the selected data row
If one (or more) coder is correct and you find that you can improve on the data by adding page numbers, more references or commentary - please do so. Add this content to a row which you have tagged as True for the `Select`-column.

### More than one correct data row
If you are comparing coding of more than 2 sheets, you may find that more than one row is correct and should be marked as selected. In these cases, mark True for `Select` for the coding that has the best `Source` and `Comment `fields. If there are several that are good, mark all of them as True for the `Select`-column. Mark all correct values as "correct" in classification of conflict, include those you may not "select" as the best datapoint.

### Other
Ignore any rows where the "Value" field is blank. Also ignore any features that are inactive. Inactive features can be flagged for conflicts, but they are marked as "True (inactive feature)" in the column "Conflict". You can use this to filter them out.

