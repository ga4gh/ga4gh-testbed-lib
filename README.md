<img src="https://www.ga4gh.org/wp-content/themes/ga4gh/dist/assets/svg/logos/logo-full-color.svg" alt="GA4GH Logo" style="width: 400px;"/>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.7|3.8|3.9|3.10-blue.svg?style=flat-square)](https://www.python.org/)
[![GitHub Actions](https://img.shields.io/github/workflow/status/ga4gh/ga4gh-testbed-lib/Test/main?style=flat-square)](https://github.com/ga4gh/ga4gh-testbed-lib/actions)
[![Coveralls](https://img.shields.io/coveralls/github/ga4gh/ga4gh-testbed-lib/main?style=flat-square)](https://coveralls.io/github/ga4gh/ga4gh-testbed-lib)

# GA4GH Testbed Lib

Python library for creating GA4GH testbed reports according to a harmonized, cross-workstream schema

## Installation

As a prerequisite, please ensure you have Python 3 installed on your machine.
`ga4gh-testbed-lib` is tested on the following Python versions:
* v3.7
* v3.8
* v3.9
* v3.10

`ga4gh-testbed-lib` is a library that can be imported into your Python project.
To do so, first install it via `pip`:

```
pip install ga4gh-testbed-lib
```

Note: We recommend using a Python virtual environment when building any Python project to avoid dependency conflicts with other projects on your system.

## Usage

Once installed, you may import the `ga4gh-testbed-lib` in your Python modules. We recommend only importing the `Report` class directly: 
```
from ga4gh.testbed.report.report import Report
...
report = Report()
```

More documentation to come on how to use the report library

## Test

To contribute to the testbed library, you will need to clone the repository:
```
git clone https://github.com/ga4gh/ga4gh-testbed-lib.git
```

To run tests, you will need to install test dependencies (i.e. pytest):
```
pip install -r requirements.txt
```

Tests can be run via `pytest`:
```
python -m pytest --cov
```

## Changelog

### v0.2.0
* Able to submit reports to Testbed API via standard `POST` request

### v0.1.2
* Test level entity now has a `message` attribute for capturing test result summary in a single message

## Maintainers

* GA4GH Tech Team [ga4gh-tech-team@ga4gh.org](mailto:ga4gh-tech-team@ga4gh.org)
