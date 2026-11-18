"""
login_event.py

One LoginEvent = one login attempt pulled out of an SSH log line.

This file is FULLY WRITTEN as a worked example of a class.
Read it top to bottom before starting on the other files.
Run it on its own to see what it prints.
"""


class LoginEvent:
    """Holds the details of a single login attempt."""

    def __init__(self, timestamp, ip, username, outcome, invalid_user=False, count=1):
        # __init__ runs automatically every time you create a new LoginEvent.
        # "self" is the event being created. Each line below stores one
        # piece of information on it, so you can read it back later
        # with event.ip, event.username, and so on.
        self.timestamp = timestamp        # e.g. "Dec 10 07:08:30" (text, no year)
        self.ip = ip                      # e.g. "173.234.31.186"
        self.username = username          # e.g. "webmaster" or "root"
        self.outcome = outcome            # "failed" or "accepted"
        self.invalid_user = invalid_user  # True if the log said "invalid user"
        self.count = count                # 1 normally, N for "message repeated N times"

    def is_failure(self):
        """Return True if this event was a failed attempt."""
        return self.outcome == "failed"

    def __str__(self):
        # __str__ decides what print(event) shows.
        label = "invalid user" if self.invalid_user else "user"
        return (f"{self.timestamp} | {self.outcome.upper():8} | "
                f"{label} {self.username} from {self.ip} (x{self.count})")


# This block only runs when you run THIS file directly,
# not when another file imports LoginEvent. Use it for quick tests.
if __name__ == "__main__":
    test_event = LoginEvent("Dec 10 07:08:30", "173.234.31.186", "webmaster",
                            "failed", invalid_user=True)
    print(test_event)
    print("Is it a failure?", test_event.is_failure())
