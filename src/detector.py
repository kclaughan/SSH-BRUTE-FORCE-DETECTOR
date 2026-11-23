

class BruteForceDetector:

    def __init__(self, events, threshold):
        self.events = events
        self.threshold = threshold
        self.failures_by_ip = {}   # e.g. {"173.234.31.186": 12, "5.36.59.76": 6}
        self.users_by_ip = {}      # e.g. {"173.234.31.186": {"webmaster", "admin"}}
        self.flagged = []          # e.g. [("173.234.31.186", 12), ("5.36.59.76", 6)]
                                   # most failures first

