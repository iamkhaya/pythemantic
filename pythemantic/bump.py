"""
Bump Module
"""
import os
import re

import semantic_version


def get_current_version():
    """
    Get current version from setup.py

    Returns:
        current_version: The current version of the repo
    """
    setup_file_path = os.path.join(os.getcwd(), '__init__.py')
    setup_file = open(setup_file_path, 'r')

    setup_text = setup_file.readlines()
    for line in setup_text:
        if "__version__"in line:
            version_line = line
            current_version = re.findall(r"([0-9.]*[0-9]+)", version_line)
            break
    current_version = semantic_version.Version(current_version[0])
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
        print "error"
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
    history_file.write('### History\n' + "%s\n" % change_message + current_content)
