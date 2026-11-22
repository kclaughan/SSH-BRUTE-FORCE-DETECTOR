from login_event import LoginEvent


class LogParser:

    def __init__(self, file_path):
        self.file_path = file_path
        self.events = []         # list of LoginEvent objects
        self.skipped_lines = 0   # lines that weren't a failed attempt


    def load_file(self):
        with (open(self.file_path) as f):
            for line in f:
                event=self.parse_line(line)
                if event is not None:
                    self.events.append(event)



    def parse_line(self, line):
        if "Failed password" not in line:
            self.skipped_lines += 1
            return None
        words= line.split()
        timestamp =  " ".join(words[0:3])
        ip = words[-4]
        username= words[-6]
        invalid_user = "invalid user" in line
        return LoginEvent(timestamp,ip,username,"failed", invalid_user,)


    def get_events(self):
        """Return the list of LoginEvent objects."""
        return self.events


