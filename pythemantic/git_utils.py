"""
GitPython utility methods
"""
import os

from git import Repo, exc



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
    Check the current branch

    Returns:
        True if branch is Master, False otherwise

    """
    branch = repository.active_branch.name
    return bool(branch == "master" or  branch == "main")


def update_tags(repo, current_version, new_version, tag_message):
    """
    Tags and commits changes
    """
    try:
        repo.create_tag(new_version, repo.active_branch.name, message=tag_message)
        repo.remote('origin').push()
    except exc.GitCommandError:
        print("Ooops.. An error occured creating the tag")
        raise ValueError("Ooops.. An error occured creating the tag")
    
    repo.git.add("History.md")
    repo.index.commit("Version bump from %s to %s" % (current_version, new_version))
