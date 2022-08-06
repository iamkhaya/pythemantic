#!/usr/bin/python
"""
Pythemantic Module
"""
import sys
import bump
import bcolors
import interactions
import git_utils




def main():
    """
    """
    repo = git_utils.init_repository()

    while True:
        if git_utils.on_master_branch(repo):
            try:
                # embed()
                release_type = interactions.display_menu()
                break
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        else:
            print(bcolors.FAIL + "***** You are not on master ***** \nIt is not recommended to create releases from a branch unless they're maintenance releases\nExiting ..." + bcolors.ENDC)
            exit()

    current_version = bump.get_current_version()

    new_version = bump.bump_version(release_type, current_version)

    change_summary = interactions.add_changes()
    bump.update_history(new_version, change_summary)
    tag_message = interactions.get_tag_message()

    git_utils.update_tags(repo, current_version,
                    new_version, tag_message)
    print("Repo successfully bumped from %s to %s " % (current_version, new_version))



if __name__ == '__main__':
    sys.exit(main())
