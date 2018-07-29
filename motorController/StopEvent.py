from Event import *

class StopEvent(Event):
    def __init__(self,name,duration):
        direction = 0
        super().__init__(name,direction,duration)
        