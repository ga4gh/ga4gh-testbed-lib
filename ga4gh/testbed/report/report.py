# -*- coding: utf-8 -*-
"""This module defines the "Report" class"""

import datetime
import json
from ga4gh.testbed.report.constants import SCHEMA_NAME, SCHEMA_VERSION, TIMESTAMP_FORMAT
from ga4gh.testbed.report.phase import Phase
from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_timestamps import HasTimestamps
from ga4gh.testbed.mixins.has_summary import HasSummary

class Report(HasTimestamps, HasStatus, HasSummary):
    """Top-level class for an overall testbed report

    Contains the statuses of all tests for a single iteration of a testbed
    application. The testbed app should output a single report (in JSON) each
    time it is run. Also contains summary information about the testbed itself
    and the platform/services the testbed was run against.

    Attributes:
        schema_name (str): string constant indicating the name of the JSON
            schema associated with the Report structure
        schema_version (str): string constant indicating version of the Report
            schema
        testbed_name (str): short name describing the testbed app that produced
            the report
        testbed_version (str): release/version number of the testbed app
        testbed_description (str): longer description of the testbed
        platform_name (str): short name describing the platform/services/network
            that the testbed ran against and evaluated
        platform_description (str): longer description of the tested platform
        input_parameters ({str:str}): key-value mapping of the exact inputs
            provided to the testbed. Secure data can be obfuscated in the final
            report
        phases (Phase): list of test phases associated with this report
    """

    # read-only attributes
    FINAL_ATTRS = set([
        "schema_name",
        "schema_version"
    ])

    SUMMARY_SUBCOMPONENT_ATTR = "phases"
    SUMMARY_SUBCOMPONENT_CLASS = Phase

    def __init__(self):
        self.schema_name = SCHEMA_NAME
        self.schema_version = SCHEMA_VERSION
        self.testbed_name = ""
        self.testbed_version = ""
        self.testbed_description = ""
        self.platform_name = ""
        self.platform_description = ""
        self.input_parameters = {}
        
        self._HasTimestamps__initialize_timestamps()
        self._HasStatus__initialize_status()
        self._HasSummary__initialize_summary()

        self.phases = []
    
    def __setattr__(self, name, value):
        """Setter override prevents overwriting of read-only attributes"""

        if hasattr(self, name):
            if name in Report.FINAL_ATTRS:
                raise Exception("Cannot alter property: " + name)
        
        self.__dict__[name] = value
    
    def get_schema_name(self):
        return self.schema_name

    def get_schema_version(self):
        return self.schema_version
    
    def set_testbed_name(self, testbed_name):
        self.testbed_name = testbed_name
    
    def get_testbed_name(self):
        return self.testbed_name
    
    def set_testbed_version(self, testbed_version):
        self.testbed_version = testbed_version
    
    def get_testbed_version(self):
        return self.testbed_version
    
    def set_testbed_description(self, testbed_description):
        self.testbed_description = testbed_description
    
    def get_testbed_description(self):
        return self.testbed_description
    
    def set_platform_name(self, platform_name):
        self.platform_name = platform_name
    
    def get_platform_name(self):
        return self.platform_name
    
    def set_platform_description(self, platform_description):
        self.platform_description = platform_description
    
    def get_platform_description(self):
        return self.platform_description
    
    def add_input_parameter(self, key, value):
        """Add a single input parameter to the dictionary

        Args:
            key (str): input parameter key/name
            value (str): value of the input parameter at the given key
        """

        self.input_parameters[key] = value
    
    def add_secure_input_parameter(self, key):
        """Indicate that secure data was provided, obfuscating the value itself

        Adds the input parameter key to the dictionary, while using "[SECURE]"
        to denote that the param's value is sensitive

        Args:
            key (str): input parameter key/name
        """

        self.input_parameters[key] = "[SECURE]"
    
    def remove_input_parameter(self, key):
        """Remove a single input parameter from the dictionary

        Args:
            key (str): name of parameter to remove
        """

        del self.input_parameters[key]
    
    def add_phase(self):
        """Add a new phase object to the list

        Returns:
            Phase: the newly created phase object
        """

        phase = Phase()
        self.phases.append(phase)
        return phase
    
    def get_phases(self):
        return self.phases
    
    def get_phase(self, i):
        """Retrieve a single phase by its position in the phases list

        Args:
            i (int): index for the phase of interest
        
        Returns:
            Phase: the phase object at the specified index
        """

        return self.phases[i]
    
    def finalize(self):
        self._HasSummary__summarize()
        self.__nested_set_status()
    
    def __nested_set_status(self):
        for phase in self.get_phases():
            for test in phase.get_tests():
                test._HasSummary__set_status_from_summary()
            phase._HasSummary__set_status_from_summary()
        self._HasSummary__set_status_from_summary()
    
    def to_json(self, pretty=False):
        """Ouput the entire report as JSON

        Args:
            pretty (bool): If true, pretty-print the JSON (indents, new lines).
                default false
        """

        default_lambda = lambda o: o.__dict__
        if pretty:
            return json.dumps(self, default=default_lambda, indent=4)
        return json.dumps(self, default=default_lambda, separators=(",",":"))