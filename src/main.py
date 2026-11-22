
import os
from log_parser import LogParser
from detector import BruteForceDetector


def get_log_path():
    while True:
        path = (input("Copy and Paste File Path: "))
        if os.path.exists(path):
            return path
        else:
            print("File not found")





def get_threshold():
    while True:
        answer = (input("Flag Ip Address with more than how many attempts? "))
        try:
            number = int(answer)
            if number > 0:
                return number
            else:
                print("Value must be above 0")
        except ValueError:
            print("Please enter a whole number")



def main():
    print("==   SSH Brute Force Detector     ==")
    log_path = get_log_path()
    threshold = get_threshold()

    parser = LogParser(log_path)
    parser.load_file()
    events = parser.get_events()

    print("Failed Attempts Found:", len(events))

    detector = BruteForceDetector(events,threshold)
    detector .count_failures()
    detector.find_targeted_users()
    detector.flag_suspicious()

    print("IPs To Watch: Suspected Suspicious")
    for ip, failures in detector.flag_suspicious():

        print(ip,"-", failures,"-","Failed Attempts = ")
if __name__=="__main__":
    main()




