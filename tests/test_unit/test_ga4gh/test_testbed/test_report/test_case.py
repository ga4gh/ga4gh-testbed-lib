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

case_log_messages_inputs = "log_messages"
case_log_messages_cases = [
    (
        [
            "beginning API test case 0",
            "executing API request",
            "comparing response to expected output",
            "no differences between response and expected detected"
        ]
    )
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

@pytest.mark.parametrize(case_log_messages_inputs, case_log_messages_cases)
def test_case_log_messages(log_messages):
    case = Case()
    for log_message in log_messages:
        case.add_log_message(log_message)
    
    returned_log_messages = case.get_log_messages()
    for i in range(0, len(log_messages)):
        assert returned_log_messages[i] == log_messages[i]
