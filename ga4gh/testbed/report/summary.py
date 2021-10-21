class Summary(object):

    def __init__(self):
        self.unknown = 0
        self.passed = 0
        self.warned = 0
        self.failed = 0
        self.skipped = 0
    
    def increment_unknown(self, n=1):
        self.unknown += n
    
    def get_unknown(self):
        return self.unknown
    
    def increment_passed(self, n=1):
        self.passed += n
    
    def get_passed(self):
        return self.passed
    
    def increment_warned(self, n=1):
        self.warned += n

    def get_warned(self):
        return self.warned
    
    def increment_failed(self, n=1):
        self.failed += n

    def get_failed(self):
        return self.failed
    
    def increment_skipped(self, n=1):
        self.skipped += n

    def get_skipped(self):
        return self.skipped
    
    def aggregate_summary(self, summary):
        self.increment_unknown(n=summary.get_unknown())
        self.increment_passed(n=summary.get_passed())
        self.increment_warned(n=summary.get_warned())
        self.increment_failed(n=summary.get_failed())
        self.increment_skipped(n=summary.get_skipped())
