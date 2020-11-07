import time
import datetime


def main():

    start_datetime = datetime.datetime.now()
    print("TestProgram started: {}".format(start_datetime))

    count = 0
    while True:
        curr_datetime = datetime.datetime.now()
        print("\tcount: {}\trunning: {}".format(count, curr_datetime))
        time.sleep(.2)
        count += 1


main()
