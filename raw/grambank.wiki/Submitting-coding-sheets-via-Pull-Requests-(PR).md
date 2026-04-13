## Introduction

This is a document outlining the basic workflow for data sheet submission in the Grambank project. These instructions are for internal coders, for external collaborators who want to contribute please see this [article](https://github.com/grambank/grambank/wiki/Contribute).

Coders and node leaders submit coding sheets to Grambank via Git Pull Requests (PR). The coding sheet is then automatically checked to make sure it does not contain any formatting or referencing errors. If there are any errors, the coder receives a message in the PR thread and is asked to make the appropriate changes or supply additional information. Once these changes are made in the PR, they are approved and the sheet is incorporated into the dataset.

In this article, coders can find some information on this process. It briefly introduces GitHub, how to create a pull request (PR), which checks we run on submitted sheets, and how you can make requested edits in the PR thread.

If you have any questions, you can email gbc_support@eva.mpg.de, Johannes or Hedvig will respond to your questions.

## GitHub and Git

GitHub is a platform for collaborative software development. It provides hosting and an interface for projects using Git. Git is a version control system that allows collaborators to efficiently track changes made to a project. Git works with **repositories**, also called **repos**, which are storage spaces where projects live and where all of its files as well as metadata on the changes to the project over time are stored. Some of the central functions of Git are the ability to make **branches** of a repository, to **commit changes** to a branch and to create **Pull Requests (PR)** to **merge** a branch with the **main** (the main branch used to be called the **master**, [a term that has now been abandoned by GitHub](https://www.bbc.com/news/technology-53050955)).

Git users can make **branches** within a repository, which allows them to make changes to the files independently of other users. After they changed a file, they commit these changes to their own branch. Once a user is satisfied with the content of their branch, they can merge their branch with the main branch. This is called a Pull. Below is a screenshot from a part of the network illustrating the Grambank repos. The black line is our main branch. The points are commits (changes). The green and blue are new branches. The branches get changes (commits) and then they get pulled into main. Members of Grambank can see the full network graph for our repos [here](https://github.com/glottobank/Grambank/network).

![Screenshot 2024-04-12 at 13 31 21](https://github.com/grambank/grambank/assets/5327845/ff1fab15-92e3-4ae2-a6ea-6bff0bdbad51)

In the Grambank's GitHub repository, the main branch is **protected**. This means that changes to the main branch need to be reviewed before they can be implemented. Users can make new branches, make changes in those branches (commits) and ask for those changes to be pulled in. This is accomplished via Pull Requests, which need to be reviewed and approved before merging. Reviewers perform [quality checks](https://github.com/grambank/grambank/wiki/Automatic-quality-checks) on any incoming changes.

Git, the version control system, is often used with the command line and can be used locally on just one computer. **GitHub** provides additional functionalities on top of basic Git, including the ability to discuss [issues](https://github.com/glottobank/Grambank/issues), to add a [wiki](https://github.com/grambank/grambank/wiki) to a project, and to use the web interface or the GitHub desktop app to carry out actions that are otherwise done with the command line.

Pull requests (PRs) can be submitted to GitHub in 3 different ways:

* Through the GitHub web browser interface
* Through the GitHub desktop app
* Via the command line

The remainder of this page outlines how to make PR with each of these methods. Coders are advised to select the one that is the most convenient to them. Common to all workflows is that the submitted files should be correctly named and formatted. We recommend coders to use either the web browser interface or the GitHub desktop app.

For the overall workflow of Grambank (not just PRs), go [here](https://github.com/grambank/grambank/wiki/Basics-of-coding-Grambank#general-workflow).

## Before submitting a sheet: basic checks

Before submitting a sheet, coders should make sure that

1. The **file is correctly named**. It should be named as follows: '**CODERACRONYM_glottocode**'. For example, if Alena Witzlack-Makarevich has coded the language Amkoe for the Grambank questionnaire, her coder acronym is AWM, and the glottocode for Amkoe is hoaa1235, the file should be called "AWM_hoaa1235.tsv". 
2. Just like [the blank coding sheet](https://github.com/grambank/grambank/blob/master/docs/Grambank_most_updated_sheet.tsv), the file should be in a plain text format (UTF8) with tabs separating the columns. If you have opened the file in Excel, make sure it is saved as it was opened and not as `xlsx`.
3. The end of the filename, the file extension should be `.tsv` or `.csv`, not `.xlsx`, `.odt` etc. 
4. In **every row where there is something in the "Value" column, there should be something in the "Source" column** and vice versa.
5. In **every row where there is something in the "Comment" column, there should be something in the "Value" column**.
6. There are **no columns that have missing headers**.
7. The **allowable characters** in the Value column are either **0, 1, ?, 2, 3 and 4**. '1?' and other combinations are _not_ allowed.
8. Citations are in line with [this format](https://github.com/grambank/Grambank/wiki/Referencing-sources-in-Grambank).

All submitted coding sheets are evaluated by pygrambank commands, [see more here](https://github.com/grambank/grambank/wiki/Automatic-quality-checks).

**Some notes on file naming**:

* Coders can find their acronym [here](https://github.com/Glottobank/Grambank/blob/master/CONTRIBUTORS.md).
* Note that there is **an underscore** between the coder's name and the glottocode (not a hyphen or a space). 
* If there is more than one main coder, the acronyms should be separated with dashes. For example, "CB-PE_acha1250.tsv" is coded by CB and PE. 
* In revised sheets, coders do not add their acronym to the file name. They add a new column "Contributed_Datapoints" and add their acronym in that column to each feature they contributed to. See [this page](https://github.com/grambank/grambank/wiki/Revising-existing-coding) for more on revisions.

**Some notes spreadsheet programs**

* Coders can use any spreadsheet editing program (Numbers, Excel, Google Spreadsheets, OpenOffice, etc). However, **we recommend using the Open Source program [Libreoffice](http://www.libreoffice.org)**. It is similar in layout and functions to Excel, but it is more explicit when it comes to saving and reading in files. This reduces the chance that something goes wrong with character encoding.
* See [this guide](https://support.microsoft.com/en-us/office/save-a-workbook-to-text-format-txt-or-csv-3e9a9d6c-70da-4255-aa28-fcacf1f081e6) on how to save as tsv or csv-files in **Excel**. 
* If the file is saved as .csv, it will be converted to .tsv before it is merged.

If you use Excel and have for example French as the default language on your machine, it will save csv-files with semi-colons instead of commas. This introduces problems when we use semi-colons elsewhere. Tabs on the other hand, which is what tsv-files use, are not as easily mixed up with other characters.

The _easiest_ way to conform to the technical specifications is to use Libreoffice and open the [the blank coding sheet](https://github.com/grambank/grambank/blob/master/docs/Grambank_most_updated_sheet.tsv) as a tsv-file and save it as a tsv-file. If you make it into a csv, Excel or ods-file in between you can introduce complications. You can still filter and hide columns when you open tsv-files in Libreoffice, it just won't remember it next them you open it.

**Some notes on encoding**
We use basic utf-8 character encoding. If you use Libreoffice, you will see this when you open a sheet and set specifications when you first save a sheet. 

UTF-8 can accommodate essentially all non-ASCII characters (basically letters besides A-z) you may want to use. However, if you save it in non-UTF-8 it is possible that problems arise when converting to UTF-8.

If you can avoid it, please don't use smart quotes. And please do not use line breaks inside cells.

**A note on sources**

If you are using a source that is not indexed by Glottolog, please provide as much information as possible about the source while submitting the PR. Read more about referencing sources [here](https://github.com/glottobank/a/wiki/Referencing-sources-in-Grambank).

## Using the GitHub web browser interface

1) In a web browser, log into GitHub and in the Grambank repository navigate to the folder called [original_sheets](https://github.com/Glottobank/Grambank/tree/master/original_sheets).

2) In the top right corner, click "Add file" and choose "Upload files" from the dropdown menu.

3) Drag and drop the coding sheets you are submitting into the web browser window.

4) In the "Commit changes" box, provide a brief but informative description of the changes, for example "fixed typo in source", "submitting coding for Kam", or "corrected coding for GB123 from 0 to 1".

5) Under the text boxes, tick the option "Create a new branch for this commit and start a pull request." Change the branch name to something unique and descriptive.

6) click "Propose changes". 

7) In the right sidebar, select @johenglisch and @HedvigS as reviewers.

8) Click "Create pull request". This will create a PR with an associated thread.

9) The reviewers will merge and delete branches as appropriate. If everything is alright, the PR will be reviewed and merged without requests for revisions. If there are comments or additional requests by the reviewers, they will comment in the thread. Revisions can then be made in the thread.

## Using the GitHub desktop app

If you have not already downloaded the GitHub desktop app, you can download it [here](https://desktop.github.com). 

### Cloning in GitHub desktop
If you have not already cloned the Grambank repository, under the "File" menu, click "Clone repository". Under the GitHub.com tab, search for the repos called "glottobank/Grambank". Make sure the "Local path" points somewhere that makes sense to you on your computer. You will now have a folder on your computer called "grambank" that will have all the contents of the Grambank repository, similar to what you see under [the "Code" tab](https://github.com/glottobank/Grambank) in the web browser interface.

### Adding new files via the GitHub desktop app
1) In the top menu in the GitHub desktop app, click the "Branch" menu and select "New branch". Name the branch with your GitHub username and a short representative title, i.e. "HS submit hoaa1235". Make sure that the "Current branch" tab in the interface lists your new branch.

2) Move or copy the coding sheet to the folder called "original sheets" in the cloned repository on your machine. If you are making changes to an existing sheet, edit that file in the "original sheets" folder.

3) Go back to GitHub desktop. The app will automatically detect any changes that were made to the local clone. Check whether the changes that are listed for the Grambank repos are indeed the changes you made in the sheets that you want to submit.

4) In the "Commit changes" box in the left bottom corner, provide a brief but informative description of the changes, for example "fixed typo in source", "submitting coding for Kam", or "corrected coding for GB123 from 0 to 1". Click "Commit to [name of branch]".

5) Click "Publish branch" in the main window.

6) Click "Create pull request". This will open a browser window and a pull request thread on GitHub.

7) Select @johenglisch and @HedvigS as reviewers.

8) Click "Create pull request". This will create a PR with an associated thread.

9) The reviewers will merge and delete branches as appropriate. If everything is alright, the PR will be reviewed and merged without requests for revisions. If there are comments or additional requests by the reviewers, they will comment in the thread. Revisions can then be made in the thread.

## Using the command line

1) Using Terminal or Command prompt, use Bash to navigate to the local clone of the glottobank/Grambank repository on your computer.

2) Create a new branch, maybe using the glottocode of the new sheet as BRANCH_NAME.

```bash
git checkout -b BRANCH_NAME
```

4) Copy your sheet to the `original_sheets` directory.

5) Add your sheet to the repository.

```bash
git add original_sheets/YOUR_SHEET
```

6) Commit the changes.

```bash
git commit -a -m "added sheet for GLOTTOCODE"
```

7) Push your changes to GitHub.

```bash
git push origin BRANCH_NAME
```

GitHub will accept the push sending back some info, including how to create a PR now, similar to

```
remote: Create a pull request for 'BRANCH_NAME' on GitHub by visiting:
remote:      https://github.com/glottobank/Grambank/pull/new/BRANCH_NAME
```

8) Create the PR, selecting @johenglisch and @HedvigS as reviewers.

9) The reviewers will merge and delete branches as appropriate. If everything is alright, the PR will be reviewed and merged without requests for revisions. If there are comments or additional requests by the reviewers, they will comment in the thread. Revisions can then be made in the thread. 

# Revision needed

Once you have filed the PR, in any of the three ways listed above ([web browser](https://github.com/grambank/grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-%28PR%29/#using-the-github-web-browser-interface), [GitHub desktop app](https://github.com/grambank/grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-%28PR%29/#using-the-github-desktop-app) or [Git command line](https://github.com/grambank/grambank/wiki/Submitting-coding-sheets-via-Pull-Requests-%28PR%29/#using-the-command-line), a review will be started and with it a conversation. [Here is an example.](https://github.com/glottobank/Grambank/pull/2708) This review may result in changes being necessary. For example, if a data sheet fails one of our [automatic quality checks](https://github.com/grambank/grambank/wiki/Automatic-quality-checks) this needs to be remedied. 

When you submit a PR and something needs to be changed in order for it to be approved, you have two choices:

1) tell the reviewer in a message in the PR thread what the change needs to be and they make the adjustments for you. For example, in [this PR](https://github.com/glottobank/Grambank/pull/2690) there was some issues with the sources. [Johannes pointed this out](https://github.com/glottobank/Grambank/pull/2690#issuecomment-1882697147), [Janis wrote a message giving the solution](https://github.com/glottobank/Grambank/pull/2690#issuecomment-1882770870) and [Johannes implemented the solution by editing our bibliography file](https://github.com/glottobank/Grambank/pull/2690/commits/454f708ce86b1fcfc1bf31c91d1b5fe19fd3eb4c). The problem was addressed and the PR could be merged in.
2) edit the file(s) yourself to make the necessary changes.


## tell the reviewer what edits to make
If you tell the review what edits to make it is good if you follow these rules:

* don't use your email client to reply. If you have email notifications from GitHub set up for your user account, you will receive emails when there are messages in your PR. You can reply to this email, but it is preferable if you click the link labelled `view it on GitHub` in the email and continue in the GitHub.com interface
* avoid uploading new files in messages in the PR. If you want to change the file, see the section below. Otherwise, it is often easier for the reviewers if you write in plain text what the new feature value should be, what the comment should be, what the missing source is etc.

## edit files yourself
If you want to edit the file(s) yourself to remedy the issues at hand, you will need to access and edit the file as it exists on the cloud branch, *not* your most recent local copy. It is not recommended to start over with a new PR or to just submit the local file again with the changes. It is possible that after you submitted the file originally, we've had to make some changes to it already. For example, you might have submitted a file with the wrong extension (.`txt` instead of `.tsv`), in the wrong format altogether (`xlsx` or `csv` instead of a `tsv`-file). [Here is a PR where Johannes has converted the files from csv to tsv after initial uploading.](https://github.com/glottobank/Grambank/pull/2710) There might have been trouble with the character encoding so that we've had to change the file in order for the words to render correctly. A common change is that some spreadsheet programs insert new rows with no content between each original row, and we prefer to remove that ([example](https://github.com/glottobank/Grambank/pull/2181/commits/2f02060149c96068d408185a4b0023de43a62df2)). All of these changes would have happened *after* you made the initial upload. The file in the cloud would have changed, and it could therefore be different from your local file. Therefore it is necessary to edit the most recent version of the file on the cloud as opposed to your local copy.

If you want to edit the file(s) yourself, you will therefore need to edit the file your new branch in the cloud. Regardless of which approach you choose, there will be a new branch created that contains your changes (for example file additions). The PR is the workflow by which we review your new branch and decide if we should pull these changes into the main branch. You can view this new branch of yours separately from the Pull Request, it'll exist as one branch in our repos ([see list of all branches here](https://github.com/glottobank/Grambank/branches)). If you don't know the name of your branch, you can find it at the top of your Pull Request (see screenshot below).

![Screenshot 2024-04-12 at 12 19 12](https://github.com/grambank/grambank/assets/5327845/046ac6b3-a7de-4cc5-afa3-fc98aad75a27)

The steps are
* find the name of your new branch
* decide if you're using GitHub web browser, GitHub desktop or Git Command Line
* if GitHub web browser
  - click on your branch in [the list of branches](https://github.com/glottobank/Grambank/branches) or on top of the PR thread
  - find the relevant file you want to edit
  - follow these instructions a) [for very small changes](https://github.com/grambank/grambank/wiki/Revising-existing-coding#edit-in-the-web-browser) and b) [these ones for larger changes](https://github.com/grambank/grambank/wiki/Revising-existing-coding#download-and-edit-locally). When you re-upload the files with larger changes, make sure you're in the right branch (not the main branch but your new branch) 

* if GitHub desktop
  - click "Pull Requests", find your PR and click it. This will fetch the correct branch.
![Screenshot 2024-04-12 at 13 17 07](https://github.com/grambank/grambank/assets/5327845/51bcd5ff-9883-4903-9153-63645fb97f4e)
  - make changes locally
  - go back to GitHub Desktop, commit changes and push
  - your changes will now appear in the PR thread.
