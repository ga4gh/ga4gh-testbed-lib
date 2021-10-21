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