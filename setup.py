import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_version():
    VERSIONFILE = os.path.join('pythemantic', '__init__.py')
    initfile_lines = open(VERSIONFILE, 'rt').readlines()
    for line in initfile_lines:
        current_version = re.findall(r"([0-9.]*[0-9]+)", line)
        return current_version[0]
    raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))

config = {
    'description': 'Pythemantic',
    'author': 'Khayelihle Tshuma',
    'url': 'https://github.com/iamkhaya/pythemantic',
    'download_url': 'https://github.com/iamkhaya/pythemantic',
    'author_email': 'khayelihle.tshuma@gmail.com',
    'version': get_version(),
    'install_requires': ['nose', 'gitpython', 'semantic_version'],
    'packages': [],
    'scripts': [],
    'name': 'pythemantic'
}
setup(**config)
