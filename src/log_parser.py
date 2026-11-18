"""
log_parser.py

LogParser reads an OpenSSH log file and turns the lines you care about
into LoginEvent objects.

YOUR JOB: replace each `raise NotImplementedError(...)` with real code.
Each method's docstring says what it must do. The hints point the way.
"""

from login_event import LoginEvent


class LogParser:

    def __init__(self, file_path):
        self.file_path = file_path
        self.events = []         # list of LoginEvent objects
        self.skipped_lines = 0   # lines that weren't a failed attempt

    def load_file(self):
        """
        Open self.file_path and send every line to parse_line().
        If parse_line() gives back an event (not None), add it to self.events.

        Hints:
        - open() + with (Module 7). A for loop walks a file one line at a time.
        - Which error does Python raise when the file isn't there?
          Catch it with try/except and print a clear message instead of crashing.
        - Test it first by just printing each line. Then swap the print
          for the call to parse_line().
        """
        raise NotImplementedError("TODO: write load_file()")

    def parse_line(self, line):
        """
        Look at ONE line of the log.
        - "message repeated N times: [ Failed password ...]" -> LoginEvent with count=N
        - A normal failed-attempt line                        -> LoginEvent with count=1
        - Anything else -> add 1 to self.skipped_lines and return None

        Hints:
        - Check for the "repeated" line FIRST. It also contains the words of a
          normal failed line, so ask yourself: what goes wrong if you check
          the normal line first?
        - Use `in` with the words that ONLY appear on failed-attempt lines.
        - line.split() turns the line into a list of words.
        - The first 3 words are the timestamp.
        - The username moves depending on "invalid user". Try counting from
          the END of the list (negative indexes): what's always in the same place?
        - Test with ONE line copied from the log before running the whole file.
        """
        raise NotImplementedError("TODO: write parse_line()")

    def get_events(self):
        """Return the list of LoginEvent objects."""
        return self.events
