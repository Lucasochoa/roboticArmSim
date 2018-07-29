class Event(object):
    def __init__(self,name,direction,duration):
        self.name = name
        self.direction = direction
        self.duration = duration
        self.startTime = 0
        self.active = False
        self.selected = False
        self.speed = 5

    def runEvent(self,limb,timerTotal):
        if timerTotal >= self.startTime and timerTotal < \
        self.startTime+self.duration:
            limb.rotate(self.speed*self.direction)
            self.active = True
            return True
        else:
            self.active = False
            return False