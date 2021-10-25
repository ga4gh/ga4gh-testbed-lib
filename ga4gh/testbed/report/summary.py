# -*- coding: utf-8 -*-
"""Defines the "Summary" class"""

class Summary(object):
    """Summarizes the status of multiple tests

    Used to summarize the status of multiple tests beneath a component in the 
    test hierachy, for example, all the cases associated with a single test.
    Counts the number of instances of each status observed.

    Attributes:
        unknown (int): number of test subcomponents with "UKNOWN" status
        passed (int): number of test subcomponents with "PASS" status
        warned (int): number of test subcomponents with "WARN" status
        failed (int): number of test subcomponents with "FAIL" status
        skipped (int): number of test subcomponents with "SKIP" status
    """

    def __init__(self):
        self.unknown = 0
        self.passed = 0
        self.warned = 0
        self.failed = 0
        self.skipped = 0
    
    def increment_unknown(self, n=1):
        """Increase "unknown" count by 1 (default) or by specified number

        Args:
            n (int): number to increment by, default: 1
        """

        self.unknown += n
    
    def get_unknown(self):
        return self.unknown
    
    def increment_passed(self, n=1):
        """Increase "passed" count by 1 (default) or by specified number
        
        Args:
            n (int): number to increment by, default: 1
        """

        self.passed += n
    
    def get_passed(self):
        return self.passed
    
    def increment_warned(self, n=1):
        """Increase "warned" count by 1 (default) or by specified number
        
        Args:
            n (int): number to increment by, default: 1
        """

        self.warned += n

    def get_warned(self):
        return self.warned
    
    def increment_failed(self, n=1):
        """Increase "failed" count by 1 (default) or by specified number
        
        Args:
            n (int): number to increment by, default: 1
        """

        self.failed += n

    def get_failed(self):
        return self.failed
    
    def increment_skipped(self, n=1):
        """Increase "skipped" count by 1 (default) or by specified number
        
        Args:
            n (int): number to increment by, default: 1
        """

        self.skipped += n

    def get_skipped(self):
        return self.skipped
    
    def get_total(self):
        """Get the total number of tests performed according to summary

        Returns:
            (int) total number of tests performed, ie. the sum of all individual
                status counts
        """

        return self.get_unknown() + self.get_passed() + self.get_warned() \
            + self.get_failed() + self.get_skipped()
    
    def aggregate_summary(self, summary):
        """Aggregate the counts from another summary onto this summary

        Args:
            summary (Summary): another summary object, with test status counts
                to apply to this summary
        """

        self.increment_unknown(n=summary.get_unknown())
        self.increment_passed(n=summary.get_passed())
        self.increment_warned(n=summary.get_warned())
        self.increment_failed(n=summary.get_failed())
        self.increment_skipped(n=summary.get_skipped())
