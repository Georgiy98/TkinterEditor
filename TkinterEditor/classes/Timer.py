import time
import threading
from ctypes import *
class Timer():
    do          =""
    Interval    =""
    Enabled     =""
    Proccess    =""

    def __init__(self,do,Interval,event=None):
        self.Interval=Interval
        self.do=do
        self.Enabled=False
        self.Proccess=True

    def Tick(self,event=None):
        self.Enabled=True
        while self.Enabled:
            if self.Params==None:
                self.do()
            else:
                self.do(self.Params)
            time.sleep(self.Interval)

    def Tick_pause(self,event=None):
        self.Enabled=True
        while self.Enabled:
            if self.Proccess:
                if self.Params == None:
                    self.do()
                else:
                    self.do(self.Params)
            time.sleep(self.Interval)

    def Start(self,pause=False,event=None,params=None):
        self.Params = params
        if not self.Enabled:
            if pause:
                self.Proccess=True
                t = threading.Thread(target=self.Tick_pause)
            else:
                t = threading.Thread(target=self.Tick)
            t.start()

    def Pause(self,event=None):
        self.Proccess=False

    def Continue(self,event=None):
        self.Proccess=True

    def Stop(self,event=None):
        self.Enabled=False


