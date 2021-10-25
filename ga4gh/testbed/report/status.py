# -*- coding: utf-8 -*-
"""Defines the "Status" enumerated type"""

from enum import Enum

class Status(str, Enum):
    """Enumeration of possible states of a test component

    Allowed values:
        UNKNOWN: test status is not known
        PASS: test passed expectedly
        WARN: test passed with warning(s)
        FAIL: test failure
        SKIP: test was not performed
    """
    
    UNKNOWN = "UNKNOWN"
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"
    SKIP = "SKIP"
