import datetime
import time


def start_time():
    print(f"START at {datetime.datetime.now()}")


def end_time():
    print(f"END at {datetime.datetime.now()}")


start_time()
time.sleep(3)
end_time()