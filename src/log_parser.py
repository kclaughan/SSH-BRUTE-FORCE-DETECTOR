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

