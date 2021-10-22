import pytest
from ga4gh.testbed.report.summary import Summary

increment_inputs = "count_type," \
    + "use_n," \
    + "n,"
increment_cases = [
    ("unknown", False, 1),
    ("unknown", True, 3),
    ("passed", False, 1),
    ("passed", True, 4),
    ("warned", False, 1),
    ("warned", True, 5),
    ("failed", False, 1),
    ("failed", True, 6),
    ("skipped", False, 1),
    ("skipped", True, 7)
]

@pytest.mark.parametrize(increment_inputs, increment_cases)
def test_summary_increment(count_type, use_n, n):
    summary = Summary()
    
    increment_fn_name = "increment_" + count_type
    getter_fn_name = "get_" + count_type

    increment_fn = getattr(summary, increment_fn_name)
    getter_fn = getattr(summary, getter_fn_name)

    if use_n:
        increment_fn(n=n)
    else:
        increment_fn()
    
    assert getter_fn() == n