import datetime
from ga4gh.testbed.report.constants import TIMESTAMP_FORMAT

class HasTimestamps(object):

    def set_start_time(self, start_time):
        self.start_time = start_time
    
    def set_start_time_now(self):
        self.set_start_time(datetime.datetime.utcnow().strftime(TIMESTAMP_FORMAT))
    
    def get_start_time(self):
        return self.start_time
    
    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_end_time_now(self):
        self.set_end_time(datetime.datetime.utcnow().strftime(TIMESTAMP_FORMAT))
