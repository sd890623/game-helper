import threading
import time
import sys


class MyThreadA(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.event = event

    def run(self):
        while True:
            if self.event.is_set():
                print("Thread A is running...")
            else:
                print("Thread A is paused...")
            time.sleep(1)

class MyThreadB(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.clear()
            time.sleep(2)
            self.event.set()

def signal_handler(signal, frame):
    print("Exiting program...")
    sys.exit(0)

event = threading.Event()
thread_a = MyThreadA(event)
thread_b = MyThreadB(event)

# signal.signal(signal.SIGINT, signal_handler)


thread_a.start()
thread_b.start()