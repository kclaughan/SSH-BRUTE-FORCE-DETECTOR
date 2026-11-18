"""
report_writer.py

ReportWriter saves the detector's results to files. This is WEEK 3 work:
get parsing, counting and flagging working first.

YOUR JOB (later): replace each `raise NotImplementedError(...)` with real code.
"""


class ReportWriter:

    def __init__(self, detector, output_folder):
        self.detector = detector
        self.output_folder = output_folder

    def write_text_report(self):
        """
        Write report.txt: each flagged IP, its failure count and the usernames it tried.

        Hints:
        - open() with "w" mode creates or overwrites a file.
        - Build the path with os.path.join(self.output_folder, "report.txt").
        """
        raise NotImplementedError("TODO: write_text_report()")

    def write_csv(self):
        """
        Write flagged_ips.csv with columns: ip, failures, usernames.

        Hints (pandas):
        - Build a list of dictionaries, one per flagged IP.
        - pandas.DataFrame(that_list), then .to_csv(path, index=False).
        """
        raise NotImplementedError("TODO: write_csv()")

    def make_chart(self):
        """
        Save top_ips.png: a bar chart of the top 10 flagged IPs.

        Hints (matplotlib):
        - Slice the first 10 of detector.flagged.
        - Two lists: IPs (labels) and failures (bar heights).
        - plt.bar(), add a title and axis labels, then plt.savefig().
        - Long IPs overlap on the x-axis. Look up plt.barh() or rotating labels.
        """
        raise NotImplementedError("TODO: make_chart()")
