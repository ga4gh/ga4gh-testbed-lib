import datetime
import json
from ga4gh.testbed.report.constants import SCHEMA_NAME, SCHEMA_VERSION, TIMESTAMP_FORMAT
from ga4gh.testbed.report.phase import Phase
from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_timestamps import HasTimestamps
from ga4gh.testbed.mixins.has_summary import HasSummary

class Report(HasTimestamps, HasStatus, HasSummary):

    FINAL_ATTRS = set([
        "schema_name",
        "schema_version"
    ])

    def __init__(self):
        self.schema_name = SCHEMA_NAME
        self.schema_version = SCHEMA_VERSION
        self.testbed_name = ""
        self.testbed_version = ""
        self.testbed_description = ""
        self.platform_name = ""
        self.platform_description = ""
        self.input_parameters = {}
        
        self.initialize_timestamps()
        self.initialize_status()
        self.initialize_summary()

        self.phases = []
    
    def __setattr__(self, name, value):
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
        self.input_parameters[key] = value
    
    def add_secure_input_parameter(self, key):
        self.input_parameters[key] = "[SECURE]"
    
    def remove_input_parameter(self, key):
        del self.input_parameters[key]
    
    def add_phase(self):
        phase = Phase()
        self.phases.append(phase)
        return phase
    
    def get_phases(self):
        return self.phases
    
    def get_phase(self, i):
        return self.phases[i]
    
    def to_json(self, pretty=False):
        default_lambda = lambda o: o.__dict__
        if pretty:
            return json.dumps(self, default=default_lambda, indent=4)
        return json.dumps(self, default=default_lambda, separators=(",",":"))