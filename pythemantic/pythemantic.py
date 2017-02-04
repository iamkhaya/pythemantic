#!/usr/bin/python
import bump
import interactions
import git_utils


class Pythemantic(object):

    def __init__(self):
        release_type = interactions.display_menu()
        repo = git_utils.init_repository()

        if git_utils.check_branch(repo):
            current_version = bump.get_current_version()
            new_version = bump.bump_version(release_type, current_version)

            change_summary = interactions.add_changes()

            bump.update_history(new_version, change_summary)
            tag_message = interactions.get_tag_message()

            git_utils.update_tags(repo, current_version, new_version, tag_message)
            print "Repo successfully bumped from %s to %s "% (current_version, new_version)
        else:
            print "Not on Master"

if __name__ == '__main__':
    pythemantic = Pythemantic()
