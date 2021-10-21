from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_timestamps import HasTimestamps
from ga4gh.testbed.mixins.has_message import HasMessage

class Case(HasTimestamps, HasStatus, HasMessage):

    def __init__(self):
        self.case_name = ""
        self.case_description = ""

        self.initialize_timestamps()
        self.initialize_status()
        self.initialize_message()
    
    def set_case_name(self, case_name):
        self.case_name = case_name
    
    def get_case_name(self):
        return self.case_name
    
    def set_case_description(self, case_description):
        self.case_description = case_description
    
    def get_case_description(self):
        return self.case_description
