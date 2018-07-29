from Event import *

class RotationEvent(Event):
    def __init__(self,name,direction,duration):
        super().__init__(name,direction,duration)

