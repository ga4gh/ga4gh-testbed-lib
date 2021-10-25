# -*- coding: utf-8 -*-
"""Defines the "Phase" class"""

from ga4gh.testbed.mixins.has_timestamps import HasTimestamps
from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_summary import HasSummary
from ga4gh.testbed.report.test import Test

class Phase(HasTimestamps, HasStatus, HasSummary):
    """A single phase of logical grouping of tests within an overall test suite
    
    Immediate subcomponent of the overall test report. Represents a single
    phase or logical grouping of tests within an overall test suite. A phase
    may correspond to all tests associated with a group of endpoints. In the
    case that the testbed is testing multiple services, a single phase could
    represent all tests associated with a single server in the network.

    Attributes:
        phase_name (str): short, unique name describing the test phase
        phase_description (str): long description of the test phase
        tests ([Test]): list of test objects associated with this phase
    """

    SUMMARY_SUBCOMPONENT_ATTR = "tests"
    SUMMARY_SUBCOMPONENT_CLASS = Test

    def __init__(self):
        self.phase_name = ""
        self.phase_description = ""

        self._HasTimestamps__initialize_timestamps()
        self._HasStatus__initialize_status()
        self._HasSummary__initialize_summary()

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
        """Add a new test object to the list

        Returns:
            Test: the newly created test object
        """

        test = Test()
        self.tests.append(test)
        return test
    
    def get_tests(self):
        return self.tests
    
    def get_test(self, i):
        """Retrieve a single test by its position in the tests list

        Args:
            i (int): index for the test of interest
        
        Returns:
            Test: the test object at the specified index
        """

        return self.tests[i]