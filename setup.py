try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {
    'description': 'Pythemantic',
    'author': 'Khayelihle Tshuma',
    'url': 'https://github.com/iamkhaya/pythemantic',
    'download_url': 'https://github.com/iamkhaya/pythemantic',
    'author_email': 'khayelihle.tshuma@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['gitpython'],
    'scripts': [],
    'name': 'pythemantic'
}
setup(**config)
