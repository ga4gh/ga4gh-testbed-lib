from enum import Enum

class Status(str, Enum):
    UNKNOWN = "UNKNOWN"
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"
    SKIP = "SKIP"
