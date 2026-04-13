These instructions are for internal coders, for external collaborators who want to contribute please see this [article](https://github.com/grambank/grambank/wiki/Contribute).

Sometimes, we need to revise existing data. Revisions come in two forms. Some revisions correct errors detected by coders, patrons, experts or automatic checks. Other revisions involve what we call 'up-coding', that is, adding data to incomplete sheets. These incomplete sheets could contain data that is imported from other datasets which do not cover every domain of grammar that Grambank covers, or they could be based on a previous version of the questionnaire. In this article, we explain how to correct errors and how to add coding to incomplete sheets.

These two things are very important:
* work on the most recent version of the file
* respond in the PR conversation as soon as possible. Don't leave us hanging if we have follow-up questions.

## What to revise

### Types of errors
These are the types of errors that we automatically detect:

* A datapoint is filled in without a cited source.
* A comment is provided but there is no coding in the 'value' column of the sheet.
* A column has a missing header.
* An illegal answer is given, i.e. an answer other than 0, 1, ? and sometimes 3 or 4, is given.
* A datapoint is duplicated.

We keep track of these automatically detectable errors in our to do lists. Coders can reserve languages by adding their name in the column "Reserved by (person)".

### Coding up: completing incomplete sheets
We inherited datapoints from other projects. Usually, in these sheets, several questions in the Grambank questionnaire were left unanswered, either because the questions did not exist in the other project or because the question in the other database [could not be translated](https://github.com/grambank/grambank/wiki/Logical-dependencies-between-features) into a Grambank question. The languages for which we have incomplete data have to be coded up. The procedure for this is very similar to that of error correction, with the difference that this also involves new coding.

## How to submit revisions

### Basics

Make sure that you **work with the latest version of the sheet** found in the ["original_sheets" folder](https://github.com/glottobank/Grambank/tree/master/original_sheets) in the main branch of the Grambank repository. If you work with GitHub Desktop, make sure you regularly Fetch and Pull the changes from the origin/master branch.

If there is more than one tsv-file with the relevant glottocode in the "original_sheets" folder, only concern yourself with the one that is indicated in the sheet-column in the to-do spreadsheet. The other files are either the result of double coding or imported from another database. When there is more than one sheet per language, we pick the one with the least missing values for the final dataset.

We recommend that you **make changes to sheets with [LibreOffice Calc](https://www.libreoffice.org/discover/calc/)**. 

Do not edit the file name of the sheet. Instead, for every row you edit, you should **add your [coder initials](https://github.com/glottobank/Grambank/blob/master/CONTRIBUTORS.md) to the "Contributed_Datapoints" column**. This applies to all kinds of changes, including improving the way a source is referenced and correcting typos in the comment-field. In cases where a feature value is changed, it is also necessary to update the comment field. This is particularly important when correcting imported datapoints. If someone else's initials are already there, just tack your abbreviation on after a space: "MM" -> "MM HS".

Before revision:

Feature_ID	|Value|	Comment|	Source	|Contributed_Datapoint	|
| ---- |  ---- |----------- |  ----------- |  ----------- |  
GB020	|0| The articles aren't obligatory|Gerard (1929:91)|
GB023	|0||Gerard (1929:99)|
GB021	|0||Gerard (1929:3)|

After revision (note that for GB023 only the source was changed not the value)

Feature_ID	|Value|	Comment|	Source	|Contributed_Datapoint	|
| ---- |  ---- |----------- |  ----------- |  ----------- |  
GB020	|1| The articles are obligatory|Gerard (1929:91)| HS|
GB023	|0||Gerard (1929:89)|HS|
GB021	|0||Gerard (1929:3)|

Do **NOT** create new columns for Value,  Comment and Source for your new revision. You should overwrite what is already there if you want to make a change. Because we use Git for version-control, we can *always* access older versions of the file and retrieve old data.

Do **NOT** edit the filename. Do not add your coder initials to the filename.

Do **NOT** reorder the rows of the spreadsheet. If you re-order the rows, that is interpreted by the Git version history as a series of deletions and a series of insertions. This is very difficult to untangle later. Do not change the order of rows or columns.

If you re-evaluate existing coding, **indicate this in the comment section** by typing a comment relating to the specific situation (for example, "no mention of gender" or "pronouns do not mark masc/fem"). If there is an "autotranslated" comment and you have investigated the issue on your own, **remove the "autotranslated" part** and replace it with a new comment. 

You can **use the web browser interface, the desktop client or the command line to update existing sheets**. In the remainder of this article, we go through the necessary steps for the web browser and desktop client.

### Using the GitHub web browser

When using the GitHub web browser interface to edit existing files you will first have to locate the file you are changing.

In our to do-list for revisions, we list the names of the files to be revised. All files are inside the folder `original_sheets`. The URL for your specific file will be 

`https://github.com/glottobank/Grambank/tree/master/original_sheets` + `name of specific file`

Example: [https://github.com/glottobank/Grambank/blob/master/original_sheets/RSC_samo1303.tsv](https://github.com/glottobank/Grambank/blob/master/original_sheets/RSC_samo1303.tsv)

You can also find the file by using the web browser search, which is called `Go to file`.

![Screenshot 2024-04-12 at 12 56 21](https://github.com/grambank/grambank/assets/5327845/711af462-3e49-471d-b844-52dd06349f89)

You are in the main branch now, as you can see by the `master` in `Grambank/blob/master/`. If you were in another branch, the name of that branch would occur in that position in the URL.

Once you have located the file, you have two options: 1) edit in the web browser directly or 2) download the file, edit on your local machine. 

#### Edit in the web browser 

You can edit the file directly in the web browser interface by clicking the pencil symbol. We do _not_ recommend this (except for very small edits which you know **precisely** where they are). This is because you will view the file as a raw text-file, the columns won't be aligned. The tabs that define the columns will be there, but the text will not be aligned. It is easy to make a mistake with the alignment of tabs when viewing the file in the interface in this way. If you do use the web browser interface to edit directly, only use it for very small edits (e.g. one typo that you know exactly where it is). 

Clicking the edit button:
![Screenshot 2024-04-12 at 12 57 53](https://github.com/grambank/grambank/assets/5327845/c4d20bb2-6000-4c6f-97bf-117fc40d844a)

Example of what the raw edit interface looks like:
![Screenshot 2024-04-12 at 13 12 55](https://github.com/grambank/grambank/assets/5327845/0c441e37-4fcb-43f5-8563-2496e3ab38ef)

#### Download and edit locally
If you need to make several changes to an existing file and you don't want to clone via the GitHub desktop app or command line, you can download the file from the cloud, edit and start a PR similarly to what you do for new files. 

1) **download the file** by pressing "Raw" and then, in your web browser, navigating to "File > Save as..". 
2) **Save the file** as a `tsv` file. Make sure you are saving "Page source" and remove ".txt" if it has been appended to the file name.
3) **Make changes** to the file in LibreOffice.
4) **Upload** the file to the "original_sheets" folder as you do with new files ([guidelines here](https://github.com/grambank/grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-(PR)#using-the-github-web-browser-interface))

When uploading the file, it may seem like you are adding a new file but Git knows better! Because the file is in the same folder (`original_sheets`) and has the same name as an existing file (e.g. `RSC_samo1303.tsv`), it'll understand that this is not a new file but changes to an existing file.

### Desktop client
Using the desktop client for revision is **very similar to [using it to add new files](https://github.com/grambank/grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-(PR)#using-the-github-desktop-app)**. Make sure you **regularly Fetch and Pull the changes** from the origin/master branch. Make changes to the relevant file on your machine with LibreOffice. The rest of the process - creating a new branch, committing changes, etc. - is the same as for [adding files](https://github.com/grambank/grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-(PR)#using-the-github-desktop-app).


# After-math
Once you have submitted the revised coding, there may be follow-up questions. Be sure to check in with the PR conversation after you submit the coding to answer any questions that may arise.
