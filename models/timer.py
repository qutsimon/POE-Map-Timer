import time

class Timer:

    def __init__(self, current):
        self.curr = current
        self.time = 0
        self.pause_val = 0
        self.pause = False
        self.stopped = False

    def start_timer(self, event):
        #Start pressed while not paused or stopped and running
        if self.time > 0 and self.stopped == False and self.pause == False:
            return
        self.time = time.perf_counter()
        if self.pause == True:
            self.pause = False
            return
        self.stopped = False
        self.pause_val = 0

    def return_dif(self):
        if self.time == 0:
            return 0
        if self.stopped == True or self.pause == True:
            return self.pause_val
        return time.perf_counter() - self.time + self.pause_val
        
    def timer_pause(self, event):
        self.pause_val = self.return_dif()
        self.pause = True

    def time_stop(self, event):
        self.pause_val  = self.return_dif()
        self.pause = False
        self.stopped = True

    



