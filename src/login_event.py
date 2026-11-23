

class LoginEvent:


    def __init__(self, timestamp, ip, username, outcome, invalid_user=False, count=1):
        self.timestamp = timestamp
        self.ip = ip
        self.username = username
        self.outcome = outcome
        self.invalid_user = invalid_user
        self.count = count

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
