import pytest
from ga4gh.testbed.report.case import Case

case_name_inputs = "case_name"
case_name_cases = [
    ("Query Param 1"),
    ("Query Param 2")
]

case_description_inputs = "case_description"
case_description_cases = [
    ("Test endpoint with query parameter set 1"),
    ("Test endpoint with query parameter set 2")
]

@pytest.mark.parametrize(case_name_inputs, case_name_cases)
def test_case_set_case_name(case_name):
    case = Case()
    case.set_case_name(case_name)
    assert case.get_case_name() == case_name

@pytest.mark.parametrize(case_description_inputs, case_description_cases)
def test_case_set_case_description(case_description):
    case = Case()
    case.set_case_description(case_description)
    assert case.get_case_description() == case_description
