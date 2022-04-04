import requests


class Submit():

    def __init__(self, url, series_id, series_token, report) :
        self.url = url
        self.series_id = series_id
        self.series_token = series_token
        self.report = report

    def submit_report(self):
        header = {"GA4GH-TestbedReportSeriesId": self.series_id, "GA4GH-TestbedReportSeriesToken": self.series_token}
        submit_repuest = requests.post(self.url, headers=header ,json=self.report)
        return submit_repuest.status_code
