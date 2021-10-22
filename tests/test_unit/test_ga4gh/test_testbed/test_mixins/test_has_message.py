import pytest
from ga4gh.testbed.report.case import Case

message_inputs="message"
message_cases = [
    ("Test completed successfully"),
    ("Test failed due to unspecified error")
]

@pytest.mark.parametrize(message_inputs, message_cases)
def test_message(message):
    case = Case()
    case.set_message(message)
    assert case.get_message() == message
