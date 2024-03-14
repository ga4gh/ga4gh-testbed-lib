from re import sub
import requests
import json
from ga4gh.testbed.report.report import Report

class ReportSubmitter():

    def submit_report(series_id, series_token, report:Report, url="http://localhost:4500/reports"):
        '''
        Submits a report to the GA4GH testbed api.
        
        Required arguments:
            series_id - A series ID is needed by server to group the report
            series_token - A token is needed to verify authenticity
            report - GA4GH report object
            url - URL of the testbed server
        '''
        results = {
            "status_code": None,
            "error_message": None,
            "report_id": None
        }

        if type(report) != Report:
            results["status_code"] = 400
            results["error_message"] = "Report submitted is not a GA4GH Report object"
            return results

        header = {"GA4GH-TestbedReportSeriesId": series_id, "GA4GH-TestbedReportSeriesToken": series_token}
        submit_request = requests.post(url, headers=header ,json=json.loads(report.to_json()))        

        results["status_code"] = submit_request.status_code

        if submit_request.status_code == 200:
            results["report_id"] = submit_request.json()["id"]
        else:
            if "message" in submit_request.json().keys():
                results["error_message"] = submit_request.json()["message"]

        return results
