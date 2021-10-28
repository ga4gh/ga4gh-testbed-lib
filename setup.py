import setuptools

NAME = "ga4gh-testbed-lib"
VERSION = "0.1.1"
AUTHOR = "Jeremy Adams"
EMAIL = "jeremy.adams@ga4gh.org"

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description="Python library for creating GA4GH testbed reports according to a harmonized, cross-workstream schema",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jb-adams/ga4gh-testbed-lib",
    package_data={'': ['web/*/*', 'schemas/*']},
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ),
)
