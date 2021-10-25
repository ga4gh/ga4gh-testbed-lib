# -*- coding: utf-8 -*-
"""Defines the "HasSummary" mixin"""

from ga4gh.testbed.report.summary import Summary
from ga4gh.testbed.report.status import Status

class HasSummary(object):
    """Mixin for report components that summarize the statuses of sub-components

    Applies a "summary" object to classes that implement the mixin, as well
    as methods to summarize the report subcomponents beneath them. An object's
    summary is based on the summaries of all its subcomponents

    Attributes:
        summary (Summary): summarization of all test statuses
    """

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
        """Calculate summary based on summaries/statuses of sub-components"""

        # get the object's subcomponent list via reflection 
        self_class = self.__class__
        subcomponent_attr = getattr(self_class, "SUMMARY_SUBCOMPONENT_ATTR")
        subcomponent_class = getattr(self_class, "SUMMARY_SUBCOMPONENT_CLASS")
        subcomponent_list = getattr(self, subcomponent_attr)

        if issubclass(subcomponent_class, HasSummary):
            # if the subcomponent has a summary itself, then summarize each
            # of those through recursion first before applying the numbers to
            # this summary
            self.__summarize_recursion(subcomponent_list)
        else:
            # if the subcomponent has no summary, then it is a "case" with 
            # simply a "status"
            self.__summarize_atomic_list(subcomponent_list)
    
    def __set_status_from_summary(self):
        """Set the object's status based on the values in the summary

        Follows a simple, logical pattern for setting status to pass, warn,
        fail, skip, or unknown based on the contents of the summary
        """

        total = self.summary.get_total()

        # if any failure in summary, status is failure
        if self.summary.get_failed() > 0:
            return self.set_status_fail()
        
        # if any unknown in summary, status is unknown
        if self.summary.get_unknown() > 0:
            return self.set_status_unknown()
        
        # if any warning in summary, status is warning
        if self.summary.get_warned() > 0:
            return self.set_status_warn()
        
        # if all cases were skipped, status is skipped
        if self.summary.get_skipped() == total:
            return self.set_status_skip()
        
        # if there are only passes and skips in the summary, and there is 1
        # or more passes, then status is passed
        if self.summary.get_passed() + self.summary.get_skipped() == total:
            return self.set_status_pass()
    
    def __summarize_recursion(self, subcomponent_list):
        """Summarize subcomponents through recursion before summarizing self.

        Recursive algorithm to trawl through a report and its subcomponents
        (ie. report -> phases -> tests -> cases). Summarizes the subcomponents,
        then self summarizes.
        """

        for subcomponent in subcomponent_list:
            subcomponent.__summarize()
            self.summary.aggregate_summary(subcomponent.get_summary())
    
    def __summarize_atomic_list(self, subcomponent_list):
        """Summarize self based on statuses of subcomponents
        
        Used when a Test object is self-summarizing based on the statuses of
        its cases
        """

        for subcomponent in subcomponent_list:
            status = subcomponent.get_status()
            increment_fn_name = HasSummary.INCREMENT_FUNCTIONS[status]
            increment_fn = getattr(self.summary, increment_fn_name)
            increment_fn()
