import pytest
from ga4gh.testbed.submit.report_submitter import ReportSubmitter

sample_report = {"schema_name":"ga4gh-testbed-report","schema_version":"0.1.0","testbed_name":"refget-compliance-suite","testbed_version":"","testbed_description":"","platform_name":"","platform_description":"","input_parameters":{},"start_time":"2022-03-22T17:45:37Z","end_time":"2022-03-22T17:46:32Z","status":"PASS","summary":{"unknown":0,"passed":49,"warned":0,"failed":0,"skipped":20},"phases":[]}

submit_report_inputs = "series_id,series_token,report,url,result"
submit_report_cases = [
    (
        "1edb5213-52a2-434f-a7b8-b101fea8fb30",
        "K5pLbwScVu8rEoLLj8pRy5Wv7EXTVahn",
        sample_report,
        "http://localhost:4500/reports",
        200
    ),
    (
        "483382e9-f92b-466d-9427-154d56a75fcf",
        "l0HiRbbpjVDKc6k3tQ2skzROB1oAP2IV",
        sample_report,
        "http://localhost:4500/reports",
        200
    ),
    (
        "1edb5213-52a2-434f-a7b8-b101fea8fb30",
        "K5pLbwScVu8rEoLLj8pRy5Wv7EXTVahn",
        "",
        "http://localhost:4500/reports",
        400
    ),
    (
        "1edb5213-52a2-434f-a7b8-b101fea8fb30",
        "K5pLbwScVu8rEoLLj8pRy5Wv7EXTVahn",
        {},
        "http://localhost:4500/reports",
        500
    ),
    (
        "",
        "K5pLbwScVu8rEoLLj8pRy5Wv7EXTVahn",
        sample_report,
        "http://localhost:4500/reports",
        404
    ),
    (
        "1edb5213-52a2-434f-a7b8-b101fea8fb30",
        "",
        sample_report,
        "http://localhost:4500/reports",
        401
    ),
]

@pytest.mark.parametrize(submit_report_inputs, submit_report_cases)
def test_case_submit_report(series_id,series_token,report,url, result):
    submitter = ReportSubmitter
    assert submitter.submit_report(series_id, series_token, report, url) == result

