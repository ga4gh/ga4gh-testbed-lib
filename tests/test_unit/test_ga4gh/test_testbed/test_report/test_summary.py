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

summary_total_inputs = "unknown,passed,warned,failed,skipped,total"
summary_total_cases = [
    (1, 1, 1, 1, 1, 5),
    (10, 4, 6, 7, 12, 39)
]

aggregate_summary_inputs = "counts_a,counts_b,counts_exp"
aggregate_summary_cases = [
    (
        [1, 3, 5, 7, 9],
        [2, 4, 6, 8, 10],
        [3, 7, 11, 15, 19]
    ),
    (
        [15, 9, 6, 12, 13],
        [42, 47, 31, 27, 26],
        [57, 56, 37, 39, 39]
    )
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

@pytest.mark.parametrize(summary_total_inputs, summary_total_cases)
def test_summary_get_total(unknown, passed, warned, failed, skipped, total):
    summary = Summary()
    summary.increment_unknown(n=unknown)
    summary.increment_passed(n=passed)
    summary.increment_warned(n=warned)
    summary.increment_failed(n=failed)
    summary.increment_skipped(n=skipped)
    assert summary.get_total() == total

@pytest.mark.parametrize(aggregate_summary_inputs, aggregate_summary_cases)
def test_aggregate_summary(counts_a, counts_b, counts_exp):

    def prep_summary(summary, counts):
        summary.increment_unknown(n=counts[0])
        summary.increment_passed(n=counts[1])
        summary.increment_warned(n=counts[2])
        summary.increment_failed(n=counts[3])
        summary.increment_skipped(n=counts[4])
    
    def assert_summary(summary, counts):
        assert summary.get_unknown() == counts[0]
        assert summary.get_passed() == counts[1]
        assert summary.get_warned() == counts[2]
        assert summary.get_failed() == counts[3]
        assert summary.get_skipped() == counts[4]

    summary_a = Summary()
    summary_b = Summary()
    prep_summary(summary_a, counts_a)
    prep_summary(summary_b, counts_b)
    summary_a.aggregate_summary(summary_b)
    assert_summary(summary_a, counts_exp)
