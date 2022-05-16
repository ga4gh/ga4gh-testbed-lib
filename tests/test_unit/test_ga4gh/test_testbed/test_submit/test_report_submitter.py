import pytest
from ga4gh.testbed.submit.report_submitter import ReportSubmitter
from ga4gh.testbed.report.report import Report

sample_report = Report()

submit_report_inputs = "series_id,series_token,report,url,status_code"
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
    #(
    #    "1edb5213-52a2-434f-a7b8-b101fea8fb30",
    #    "K5pLbwScVu8rEoLLj8pRy5Wv7EXTVahn",
    #    "",
    #    "http://localhost:4500/reports",
    #    400
    #),
    #(
    #    "1edb5213-52a2-434f-a7b8-b101fea8fb30",
    #    "K5pLbwScVu8rEoLLj8pRy5Wv7EXTVahn",
    #    {},
    #    "http://localhost:4500/reports",
    #    500
    #),
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
def test_case_submit_report(series_id,series_token,report,url, status_code):
    submitter = ReportSubmitter
    assert submitter.submit_report(series_id, series_token, report, url)["status_code"] == status_code

