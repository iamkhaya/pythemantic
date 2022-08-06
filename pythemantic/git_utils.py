"""
GitPython utility methods
"""
import os
from git import Repo


def init_repository():
    """
    Get current version from setup.py

    Returns:
        new_version: The bumped version

    """
    repo = Repo.init(os.getcwd())
    return repo


def on_master_branch(repository):
    """
    Check the cuurent branch

    Returns:
        True if branch is Master, False otherwise

    """
    branch = repository.active_branch.name
    print("*********" + branch)
    return bool(branch == 'master')


def update_tags(repo, current_version, new_version, tag_message):
    """
    Tags and commits changes
    """
    repo.create_tag(new_version, repo.active_branch.name, message=tag_message)
    repo.git.add("History.md")
    repo.index.commit("Version bump from %s to %s" %
                      (current_version, new_version))
