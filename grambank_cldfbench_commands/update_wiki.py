"""\
Update the subtree for the grambank wiki.

Note that git-subtree automatically add new commits to the current branch.  To
avoid merge shenanigans this script will create a new branch called update-wiki
before running git-subtree, so we can decide more easily whether to keep the
created commits for not.
"""

import re
import shutil
import subprocess
import sys

BRANCH_NAME = 'update-wiki'

from cldfbench.cli_util import add_dataset_spec, with_dataset


def register(parser):
    add_dataset_spec(parser)


def update_wiki(dataset, _args):
    git = shutil.which('git')
    if not git:
        print('git not found.', file=sys.stderr)
        sys.exit(1)

    cmd_result = subprocess.run(
        [git, '-C', dataset.dir, 'branch'],
        check=True, stdout=subprocess.PIPE)
    branch_exists = BRANCH_NAME in (
        re.fullmatch(r'[* ] (\S+)', branch_line).group(1)
        for branch_line in cmd_result.stdout.decode('utf-8').splitlines())
    if branch_exists:
        print('branch', BRANCH_NAME, 'already exists.', file=sys.stderr)
        sys.exit(1)

    subprocess.run(
        [git, '-C', dataset.dir, 'switch', '-c', BRANCH_NAME],
        check=True)
    subprocess.run(
        [git, '-C', dataset.dir, 'subtree', 'pull', '--prefix=raw/grambank.wiki',
         'https://github.com/grambank/grambank.wiki', 'master', '--squash'],
        check=True)


def run(args):
    with_dataset(args, update_wiki)
