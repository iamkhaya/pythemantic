import os
import git

def init_repository():
    repo = git.Repo(os.path.join(os.path.dirname(__file__ ), '..' ))
    return repo

def check_branch(repository):
    branch = repository.active_branch.name
    return bool(branch == 'Interactivity')

def update_tags(repo, current_version, new_version, tag_message):
    repo.create_tag(new_version, repo.active_branch.name, message = tag_message)
    repo.git.add("History.md")
    repo.index.commit("Version bump from %s to %s" %(current_version, new_version))
