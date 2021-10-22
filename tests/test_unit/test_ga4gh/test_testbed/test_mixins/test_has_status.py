import pytest
from ga4gh.testbed.report.case import Case
from ga4gh.testbed.report.status import Status

set_status_inputs = "setter,exp_status"
set_status_cases = [
    (
        "set_status_unknown",
        Status.UNKNOWN
    ),
    (
        "set_status_pass",
        Status.PASS
    ),
    (
        "set_status_warn",
        Status.WARN
    ),
    (
        "set_status_fail",
        Status.FAIL
    ),
    (
        "set_status_skip",
        Status.SKIP
    ),
]

@pytest.mark.parametrize(set_status_inputs, set_status_cases)
def test_set_status(setter, exp_status):
    case = Case()
    assert case.get_status() == Status.UNKNOWN

    set_fn = getattr(case, setter)
    set_fn()

    assert case.get_status() == exp_status
