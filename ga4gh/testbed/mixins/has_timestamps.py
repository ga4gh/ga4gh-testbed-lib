import datetime
from ga4gh.testbed.report.constants import TIMESTAMP_FORMAT

class HasTimestamps(object):

    def __initialize_timestamps(self):
        self.start_time = self.__timestamp_now()
        self.end_time = self.__timestamp_now()

    def __timestamp_now(self):
        return datetime.datetime.utcnow().strftime(TIMESTAMP_FORMAT)

    def set_start_time(self, start_time):
        self.start_time = start_time
    
    def set_start_time_now(self):
        self.set_start_time(self.timestamp_now())
    
    def get_start_time(self):
        return self.start_time
    
    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_end_time_now(self):
        self.set_end_time(self.timestamp_now())
