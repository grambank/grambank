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
6. Add/commit all changes, add the version tag, push branch to upstream and create a PR.
7. Upon acceptance, merge PR, create GitHub release from version tag.
8. Make sure the release has been picked up by Zenodo. Edit the release description on GitHub,
   adding the Zenodo citation info including DOI.

