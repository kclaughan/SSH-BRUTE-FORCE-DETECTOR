"""
detector.py

BruteForceDetector takes the list of LoginEvent objects and works out
which IPs look like brute-force attackers.

YOUR JOB: replace each `raise NotImplementedError(...)` with real code.
"""


class BruteForceDetector:

    def __init__(self, events, threshold):
        self.events = events
        self.threshold = threshold
        self.failures_by_ip = {}   # e.g. {"173.234.31.186": 12, "5.36.59.76": 6}
        self.users_by_ip = {}      # e.g. {"173.234.31.186": {"webmaster", "admin"}}
        self.flagged = []          # e.g. [("173.234.31.186", 12), ("5.36.59.76", 6)]
                                   # most failures first

    def count_failures(self):
        """
        Fill self.failures_by_ip: IP -> total failed attempts.

        Hints:
        - Loop over self.events. Only count events where is_failure() is True.
        - Add event.count, not 1. Why?
        - IP already a key? Add to it. Not there yet? Start it.
          Look up dict.get() for the short way.
        """
        raise NotImplementedError("TODO: write count_failures()")

    def find_targeted_users(self):
        """
        Fill self.users_by_ip: IP -> set of usernames that IP tried.

        Hints:
        - Same loop shape as count_failures().
        - A set ignores duplicates. Look up set() and .add().
        """
        raise NotImplementedError("TODO: write find_targeted_users()")

    def flag_suspicious(self):
        """
        Fill self.flagged with (ip, failures) pairs where
        failures >= self.threshold, sorted most failures first.

        Hints:
        - Loop over self.failures_by_ip.items(). That gives you ip AND count.
        - Build the list first, then sort it.
        - Look up sorted() with key= and reverse=True.
        """
        raise NotImplementedError("TODO: write flag_suspicious()")
