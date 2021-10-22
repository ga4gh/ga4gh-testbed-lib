import pytest
from ga4gh.testbed.report.case import Case

timestamp_inputs = "timestamp_string"
timestamp_cases = [
    ("2020-03-10T15:00:00Z"),
    ("2021-10-22T12:30:45Z")
]

@pytest.mark.parametrize(timestamp_inputs, timestamp_cases)
def test_start_time(timestamp_string):
    case = Case()
    case.set_start_time_now()
    case.set_start_time(timestamp_string)
    assert case.get_start_time() == timestamp_string

@pytest.mark.parametrize(timestamp_inputs, timestamp_cases)
def test_end_time(timestamp_string):
    case = Case()
    case.set_end_time_now()
    case.set_end_time(timestamp_string)
    assert case.get_end_time() == timestamp_string
