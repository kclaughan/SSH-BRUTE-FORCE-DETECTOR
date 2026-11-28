

class BruteForceDetector:

    def __init__(self, events, threshold):
        self.events = events
        self.threshold = threshold
        self.failures_by_ip = {}
        self.users_by_ip = {}
        self.flagged = []

    def count_failures(self):
        for event in self.events:
            ip= event.ip
            if ip in self.failures_by_ip:
                self.failures_by_ip[ip]+=1
            else:
                self.failures_by_ip[ip]=1
