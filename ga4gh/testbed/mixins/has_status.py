from ga4gh.testbed.report.status import Status

class HasStatus(object):

    def set_status_pass(self):
        self.status = Status.PASS

    def set_status_fail(self):
        self.status = Status.FAIL

    