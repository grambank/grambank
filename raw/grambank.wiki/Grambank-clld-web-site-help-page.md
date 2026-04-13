Grambank is a database that is available in a web browser interface (grambank.clld.org) and also as a CLDF-dataset archived with [Zenodo](https://zenodo.org/record/7844558) and released on [GitHub](https://github.com/grambank/grambank/releases). 

<h2> Functionalities of the web browser-interface </h2>The web browser interface is built on the CLLD framework.  </h2>

<h2> Menus </h2>
<img width="940" height="75" alt="Screenshot 2025-10-10 at 13 03 28" src="https://github.com/user-attachments/assets/320c088f-897b-4826-836c-be08f0e215d9" />

There are two horizontal menu bars at the home page. The top one (main menu) contains tabs for information about the dataset. The bottom one is a context menu to the tab "home", it does not appear for other tabs.

<h2>  Visualizing feature values on a map </h2>
Click the tab "Features" in the top menu. Select a feature. Scroll down to the heading "map".

<h2>  Combining features  </h2>
Click the tab "Features" in the top menu. Select a feature. Scroll down to a section with the sentence _You may combine this variable with a different variable by selecting on in the list below and clicking "Submit"._

Once you click "Submit", you will be taken to a new webpage with a map and table illustrating the combination of the features you selected. The URL will contain the Feature ID numbers, for example [https://grambank.clld.org/combinations/GB020_GB023](https://grambank.clld.org/combinations/GB020_GB023). If you add further Feature ID numbers to this URL, they will also be included, for example [https://grambank.clld.org/combinations/GB020_GB023_GB058](https://grambank.clld.org/combinations/GB020_GB023_GB058). 

<h2>  Visualizing feature values on a language family tree </h2>
Go to the tab "Languages and dialects" in the top menu. Click on the language family in the column "Family". At the top of the page, there is a section where you can select a feature. Once you click "Submit", you will be taken to a page showing that feature for that language family in a map and if you scroll down also on a tree, see example [here](https://grambank.clld.org/familys/aust1307?feature=GB020#tree-container). The URL will specify the language family glottocode and Grambank feature ID, you can share this URL to send others to the page.

<h2>  Further functionalities, such as comparing languages, other kinds of plotting, combining datasets, etc </h2>

The web browser interface for Grambank is just providing basic access to the dataset. For further visualizations and analysis, we suggest you [download](https://grambank.clld.org/download) the dataset and access it through python/R/spreadsheet programs etc. For advice on using R with Grambank, go [here](https://github.com/grambank/grambank/wiki/Fetching-and-analysing-Grambank-data-with-R).

<h2> General info </h2>
<h3>  Versions and citing </h3> 
The dataset is released in versions, with additions and revisions each time. If you use the dataset, please note clearly what version is used. Please see our instructions [here](https://github.com/grambank/grambank/wiki/Citing-grambank) for citing Grambank.

<h2>  Suggesting changes/additions </h2>
Please go [here](https://github.com/grambank/grambank/wiki/Contribute) for instructions on suggesting changes or additions.

<h2>  Practical information for users (including R-scripts, SQL etc) </h2> 
Please see the wiki articles [here](https://github.com/grambank/grambank/wiki#2-practical-information-for-users-and-collaborators).