# Releasing Grambank

0. Check out a new release branch `git checkout -b release-v...`.
1. Update the submodule `raw/Grambank` from remote (to an appropriate tag).
2. Update the submodule `raw/grambank.wiki` from remote.
3. Update `pygrambank` (if necessary).
4. Run
   ```shell
   cldfbench makecldf cldfbench_grambank.py --with-zenodo --with-cldfreadme --glottolog-version v...
   ```
   passing the appropriate Glottolog version.
5. Make sure the CLDF is valid:
   ```shell
   pip install -e .[test]
   pytest
   ```
6. Recreate the language map:
   ```shell
   cldfbench cldfviz.map cldf --format jpg --pacific-centered --width 20 --height 10 --output map.jpg --no-legend --with-ocean
   ```
7. Add/commit all changes, push branch to upstream and create a PR.
8. Upon acceptance, merge PR, create GitHub release thereby creating a version tag.
9. Make sure the release has been picked up by Zenodo. Edit the release description on GitHub,
   adding the Zenodo citation info including DOI.

