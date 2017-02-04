release_types = {
    'patch' : 'Patch: Bug fixes, recommended for all (default)',
    'minor' : 'Minor: New features, but backwards compatible',
    'major' : 'Major: Breaking changes'
    }


def display_menu():
    """
    Display release options to the user

    Returns:
        release_type: The type of release
    """
    prompt = '> '
    print "Enter the type of change"
    print "1. %s" % release_types['patch']
    print "2. %s" % release_types['minor']
    print "3. %s" % release_types['major']

    release_type = raw_input(prompt)
    return release_type

def add_changes():
    """
    Display prompt for summary ofchanges

    Returns:
        change_summary: A summary of the change
    """
    print "Enter the changes"
    changes = ''
    user_input = " *"
    while user_input:
        user_input = raw_input(" * ")
        changes += '\n' + '* ' + user_input
    return changes[:changes.rfind('\n')]


def get_tag_message():
    """
    Allow user to enter the tag message

    Returns:
        tag_message: A summary of the change
    """
    tag_message = raw_input(" Enter tag message : ")
    return tag_message
