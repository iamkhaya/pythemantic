"""
Bump Module
"""
import os

import semantic_version
import bcolors


def get_current_version():
    """
    Get current version from setup.py

    Returns:
        current_version: The current version of the repo
    """
    with open("version", encoding="utf-8") as f:
        version = f.read().strip()
        current_version = semantic_version.Version(version)
        return current_version

def bump_version(release_type, current_version):
    """
    Get current version from setup.py

    Returns:
        new_version: The bumped version

    """
    if release_type == '1':
        new_version = current_version.next_patch()
    elif release_type == '2':
        new_version = current_version.next_minor()
    elif release_type == '3':
        new_version = current_version.next_mijor()
    else:
        print(bcolors.FAIL + "** Invalid selection **" + bcolors.ENDC)
        return None
    return  new_version


def update_history(new_version, change_summary):
    """
    Update change_log.md or history.md file contents

    Args:
        new_version: The new version
        change_summary: A summary of all the changes in the new version

    """
    history_file_path = os.path.join(os.getcwd(), 'History.md')
    history_file = open(history_file_path, 'r')
    current_content = history_file.read()

    history_file = open(history_file_path, 'w+')
    change_message = '###### %s' % new_version + '\n' + change_summary
    history_file.write('###' + "%s\n" % change_message + current_content)
