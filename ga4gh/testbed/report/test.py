# -*- coding: utf-8 -*-
"""Defines the "Test" class"""

from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_timestamps import HasTimestamps
from ga4gh.testbed.mixins.has_summary import HasSummary
from ga4gh.testbed.mixins.has_message import HasMessage
from ga4gh.testbed.report.case import Case

class Test(HasTimestamps, HasStatus, HasSummary):
    """A single test within the reporting hierarchy, contains multiple cases

    Immediate subcomponent of a test "Phase". Represents a single test with
    multiple individual cases. A Test may correspond to all cases testing a 
    single API endpoint.

    Attributes:
        test_name (str): short, unique name describing the test
        test_description (str): longer description of the test
        cases ([Case]): list of case objects associated with this test
    """

    SUMMARY_SUBCOMPONENT_ATTR = "cases"
    SUMMARY_SUBCOMPONENT_CLASS = Case
    
    def __init__(self):
        self.test_name = ""
        self.test_description = ""
        
        self._HasTimestamps__initialize_timestamps()
        self._HasStatus__initialize_status()
        self._HasSummary__initialize_summary()
        self._HasMessage__initialize_message()
        
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
        """Add a new case object to the list

        Returns:
            Case: the newly created case object
        """

        case = Case()
        self.cases.append(case)
        return case

    def get_cases(self):
        return self.cases
    
    def get_case(self, i):
        """Retrieve a single case by its position in the cases list

        Args:
            i (int): index for the case of interest
        
        Returns:
            Case: the case object at the specified index
        """

        return self.cases[i]
