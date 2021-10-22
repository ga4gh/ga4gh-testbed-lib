# -*- coding: utf-8 -*-
"""This module defines the "Case" class"""

from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_timestamps import HasTimestamps
from ga4gh.testbed.mixins.has_message import HasMessage

class Case(HasTimestamps, HasStatus, HasMessage):
    """Atomic test report class
    
    Contains the smallest unit of information about a single test case. A case
    may correspond to a single API request with a specific set of input
    parameters, the case capturing whether the request returned the expected
    response.

    Attributes:
        case_name (str): short, unique name describing the test case
        case_description (str): longer description of the test case
        log_messages ([str]): list of helpful log messages output during the 
            test case. May be of mixed severity (debug, warning, etc.)
    """

    def __init__(self):
        self.case_name = ""
        self.case_description = ""
        self.log_messages = []

        self._HasTimestamps__initialize_timestamps()
        self._HasStatus__initialize_status()
        self.initialize_message()
    
    def set_case_name(self, case_name):
        self.case_name = case_name
    
    def get_case_name(self):
        return self.case_name

    def add_log_message(self, log_message):
        self.log_messages.append(log_message)
    
    def get_log_messages(self):
        return self.log_messages
    
    def set_case_description(self, case_description):
        self.case_description = case_description
    
    def get_case_description(self):
        return self.case_description
