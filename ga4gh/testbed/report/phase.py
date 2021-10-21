from ga4gh.testbed.mixins.has_status import HasStatus
from ga4gh.testbed.mixins.has_timestamps import HasTimestamps

class Phase(HasStatus, HasTimestamps):

    def __init__(self):
        self.phase_name = ""
        