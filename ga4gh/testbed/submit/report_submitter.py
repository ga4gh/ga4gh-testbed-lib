import requests


class ReportSubmitter():

    def submit_report(series_id, series_token, report, url="http://localhost:4500/reports"):
        '''
        Submits a report to the GA4GH testbed api.
        
        Required arguments:
            series_id - A series ID is needed by server to group the report
            series_token - A token is needed to verify authenticity
            report - GA4GH report in JSON format
            url - URL of the testbed server
        '''
        header = {"GA4GH-TestbedReportSeriesId": series_id, "GA4GH-TestbedReportSeriesToken": series_token}
        submit_request = requests.post(url, headers=header ,json=report)
        return submit_request.status_code

