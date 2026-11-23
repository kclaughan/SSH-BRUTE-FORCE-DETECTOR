

class LoginEvent:


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

        return self.outcome == "failed"

    def __str__(self):

        label = "invalid user" if self.invalid_user else "user"
        return (f"{self.timestamp} | {self.outcome.upper():8} | "
                f"{label} {self.username} from {self.ip} (x{self.count})")



if __name__ == "__main__":
    test_event = LoginEvent("Dec 10 07:08:30", "173.234.31.186", "webmaster",
                            "failed", invalid_user=True)
    print(test_event)
    print("Is it a failure?", test_event.is_failure())
