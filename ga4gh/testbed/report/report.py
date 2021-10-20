import datetime
import json
from ga4gh.testbed.report.constants import SCHEMA_NAME, SCHEMA_VERSION, TIMESTAMP_FORMAT
from ga4gh.testbed.report.status import Status
from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_timestamps import HasTimestamps

class Report(HasStatus, HasTimestamps):

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
        self.start_time = ""
        self.end_time = ""
        # self.input_parameters = ""
        self.status = Status.UNKNOWN
        # self.summary = ""
        # self.results = ""

        self.set_start_time_now()
        self.set_end_time_now()
    
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
    
    def to_json(self, pretty=False):
        default_lambda = lambda o: o.__dict__
        if pretty:
            return json.dumps(self, default=default_lambda, indent=4)
        return json.dumps(self, default=default_lambda, separators=(",",":"))
