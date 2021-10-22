from ga4gh.testbed.report.summary import Summary
from ga4gh.testbed.report.status import Status

class HasSummary(object):

    INCREMENT_FUNCTIONS = {
        Status.UNKNOWN: "increment_unknown",
        Status.PASS: "increment_passed",
        Status.WARN: "increment_warned",
        Status.FAIL: "increment_failed",
        Status.SKIP: "increment_skipped"
    }

    def get_summary(self):
        return self.summary
    
    def __initialize_summary(self):
        self.summary = Summary()
    
    def __summarize(self):
        self_class = self.__class__
        subcomponent_attr = getattr(self_class, "SUMMARY_SUBCOMPONENT_ATTR")
        subcomponent_class = getattr(self_class, "SUMMARY_SUBCOMPONENT_CLASS")
        subcomponent_list = getattr(self, subcomponent_attr)

        if issubclass(subcomponent_class, HasSummary):
            self.__summarize_recursion(subcomponent_list)
        else:
            self.__summarize_atomic_list(subcomponent_list)
    
    def __set_status_from_summary(self):
        total = self.summary.get_total()

        if self.summary.get_failed() > 0:
            return self.set_status_fail()
        
        if self.summary.get_unknown() > 0:
            return self.set_status_unknown()
        
        if self.summary.get_warned() > 0:
            return self.set_status_warn()
        
        if self.summary.get_skipped() == total:
            return self.set_status_skip()
        
        if self.summary.get_passed() + self.summary.get_skipped() == total:
            return self.set_status_pass()
    
    def __summarize_recursion(self, subcomponent_list):
        for subcomponent in subcomponent_list:
            subcomponent.__summarize()
            self.summary.aggregate_summary(subcomponent.get_summary())
    
    def __summarize_atomic_list(self, subcomponent_list):
        for subcomponent in subcomponent_list:
            status = subcomponent.get_status()
            increment_fn_name = HasSummary.INCREMENT_FUNCTIONS[status]
            increment_fn = getattr(self.summary, increment_fn_name)
            increment_fn()
