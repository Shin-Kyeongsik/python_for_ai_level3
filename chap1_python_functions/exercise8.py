import time
import datetime


def start_end_time(type):
    if type == 'start':
        print(f"START at {datetime.datetime.now()}")
    elif type == 'end':
        print(f"END at {datetime.datetime.now()}")
    else:
        print("WARNING: Unknown type")


start_end_time('start')
time.sleep(3)
start_end_time('end')