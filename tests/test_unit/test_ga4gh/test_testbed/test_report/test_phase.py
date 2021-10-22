import pytest
from ga4gh.testbed.report.phase import Phase

phase_name_inputs = "phase_name"
phase_name_cases = [
    ("Projects"),
    ("Studies"),
    ("Expressions"),
    ("Continuous")
]

phase_description_inputs = "phase_description"
phase_description_cases = [
    ("Tests the projects api"),
    ("Tests the studies api"),
    ("Tests the expressions api")
]

phase_add_tests_inputs = "test_names"
phase_add_tests_cases = [
    (
        [
            "Test project endpoint",
            "Test sequence endpoint",
            "Test service-info endpoint"
        ]
    )
]

@pytest.mark.parametrize(phase_name_inputs, phase_name_cases)
def test_phase_set_phase_name(phase_name):
    phase = Phase()
    phase.set_phase_name(phase_name)
    assert phase.get_phase_name() == phase_name

@pytest.mark.parametrize(phase_description_inputs, phase_description_cases)
def test_phase_set_phase_description(phase_description):
    phase = Phase()
    phase.set_phase_description(phase_description)
    assert phase.get_phase_description() == phase_description

@pytest.mark.parametrize(phase_add_tests_inputs, phase_add_tests_cases)
def test_phase_add_tests(test_names):
    phase = Phase()
    for test_name in test_names:
        test = phase.add_test()
        test.set_test_name(test_name)
    
    returned_tests = phase.get_tests()
    for i in range(0, len(test_names)):
        assert returned_tests[i].get_test_name() == test_names[i]
    
    for i in range(0, len(test_names)):
        assert phase.get_test(i).get_test_name() == test_names[i]
