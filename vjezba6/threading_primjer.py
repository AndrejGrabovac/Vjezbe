import _thread
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s : %s" % (threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("thread-1", 2, ))
    _thread.start_new_thread(print_time, ("thread-2", 4, ))
except:
    print("Greska: ne mogu pokrenuti niti!!")

while 1:
    pass
