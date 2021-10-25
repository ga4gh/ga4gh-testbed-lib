# -*- coding: utf-8 -*-
"""Defines the "HasTimestamps" mixin"""

import datetime
from ga4gh.testbed.report.constants import TIMESTAMP_FORMAT

class HasTimestamps(object):
    """Mixin for report components that have start and end timestamps

    Applies start and end timestamps to classes that implement the mixin, as
    well as setter and getters for each

    Attributes:
        start_time (str): ISO 8601 format string indicate test component start
        end_time (str): ISO 8601 format string indicating test component end
    """

    def __initialize_timestamps(self):
        self.start_time = self.__timestamp_now()
        self.end_time = self.__timestamp_now()

    def __timestamp_now(self):
        """Get an ISO 8601 formatted string for the current time

        Returns:
            (str): current time in ISO 8601 format
        """

        return datetime.datetime.utcnow().strftime(TIMESTAMP_FORMAT)

    def set_start_time(self, start_time):
        self.start_time = start_time
    
    def set_start_time_now(self):
        """Set start time to the current time"""

        self.set_start_time(self.__timestamp_now())
    
    def get_start_time(self):
        return self.start_time
    
    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_end_time_now(self):
        """Set end time to the current time"""
        self.set_end_time(self.__timestamp_now())
    
    def get_end_time(self):
        return self.end_time
