"""setup file"""


from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as f:
    REQUIREMENTS = [dependency.strip() for dependency in f if dependency.strip()]

with open("version", encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(
    name="pythemantic",
    version=VERSION,
    description="pythemantic",
    long_description="pythemantic library",
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
    ],
    author="Khayelihle Tshuma",
    author_email="khayelihle.tshuma@gmail.com",
    url="https://pythemantic.com",
    keywords="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
)

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
