import time
import datetime


def main():

    # random comment123

    start_datetime = datetime.datetime.now()
    print("TestProgram started: {}".format(start_datetime))

    count = 0
    while True:
        curr_datetime = datetime.datetime.now()
        print("\tcount: {}\trunning: {}".format(count, curr_datetime))
        time.sleep(1)
        count += 1


main()
