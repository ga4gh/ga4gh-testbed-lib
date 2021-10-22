import pytest
from ga4gh.testbed.report.test import Test

test_name_inputs = "test_name"
test_name_cases = [
    ("Test sequence endpoint"),
    ("Test service info endpoint"),
    ("Test metadata endpoint"),
]

test_description_inputs = "test_description"
test_description_cases = [
    ("Tests the sequence endpoint"),
    ("Tests the service info endpoint"),
    ("Tests the metadata endpoint")
]

test_add_cases_inputs = "case_names"
test_add_cases_cases = [
    (
        [
            "reference sequence e. coli",
            "reference sequence s. cerevisiae",
            "reference sequence d. melanogaster"
        ]
    )
]

@pytest.mark.parametrize(test_name_inputs, test_name_cases)
def test_test_set_test_name(test_name):
    test = Test()
    test.set_test_name(test_name)
    assert test.get_test_name() == test_name

@pytest.mark.parametrize(test_description_inputs, test_description_cases)
def test_test_set_test_description(test_description):
    test = Test()
    test.set_test_description(test_description)
    assert test.get_test_description() == test_description

@pytest.mark.parametrize(test_add_cases_inputs, test_add_cases_cases)
def test_test_add_cases(case_names):
    test = Test()
    for case_name in case_names:
        case = test.add_case()
        case.set_case_name(case_name)
    
    returned_cases = test.get_cases()
    for i in range(0, len(case_names)):
        assert returned_cases[i].get_case_name() == case_names[i]
    
    for i in range(0, len(case_names)):
        assert test.get_case(i).get_case_name() == case_names[i]
