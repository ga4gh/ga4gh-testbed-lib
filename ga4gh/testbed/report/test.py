import pytest
from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_timestamps import HasTimestamps
from ga4gh.testbed.mixins.has_summary import HasSummary
from ga4gh.testbed.mixins.has_message import HasMessage
from ga4gh.testbed.report.case import Case

class Test(HasTimestamps, HasStatus, HasSummary, HasMessage):

    SUMMARY_SUBCOMPONENT_ATTR = "cases"
    SUMMARY_SUBCOMPONENT_CLASS = Case
    
    def __init__(self):
        self.test_name = ""
        self.test_description = ""
        
        self.initialize_timestamps()
        self.initialize_status()
        self.initialize_summary()
        self.initialize_message()
        
        self.cases = []
    
    def set_test_name(self, test_name):
        self.test_name = test_name
    
    def get_test_name(self):
        return self.test_name
    
    def set_test_description(self, test_description):
        self.test_description = test_description
    
    def get_test_description(self):
        return self.test_description
    
    def add_case(self):
        case = Case()
        self.cases.append(case)
        return case

    def get_cases(self):
        return self.cases
    
    def get_case(self, i):
        return self.cases[i]
