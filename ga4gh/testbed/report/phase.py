from ga4gh.testbed.mixins.has_timestamps import HasTimestamps
from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_summary import HasSummary
from ga4gh.testbed.report.test import Test

class Phase(HasTimestamps, HasStatus, HasSummary):

    def __init__(self):
        self.phase_name = ""
        self.phase_description = ""

        self.initialize_timestamps()
        self.initialize_status()
        self.initialize_summary()

        self.tests = []
    
    def set_phase_name(self, phase_name):
        self.phase_name = phase_name
    
    def get_phase_name(self):
        return self.phase_name
    
    def set_phase_description(self, phase_description):
        self.phase_description = phase_description
    
    def get_phase_description(self):
        return self.phase_description
    
    def add_test(self):
        test = Test()
        self.tests.append(test)
        return test
    
    def get_tests(self):
        return self.tests
    
    def get_test(self, i):
        return self.tests[i]