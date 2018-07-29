from HelperFunctions import *
import math
class RadialDial(object):
    def __init__(self,x,y,size,pos,header):
        self.x = x
        self.y = y
        self.size = size
        self.nodeSize = self.size//5
        self.pos = pos
        self.header = header
        self.active = False

    def mouseClickedDown(self,event):
        x = self.x+self.size*math.cos(math.radians(self.header))
        y = self.y+self.size*math.sin(math.radians(self.header))
        if distance(x,y,event.x,event.y) < self.nodeSize:
            self.active = True

    def mouseMoved(self,event,data):
        self.header = math.degrees(math.atan(slope(self.x,self.y,\
            event.x,event.y)))
        

    def mouseReleased(self,event):
        pass

    def animate(self):
        self.header += 1

    def draw(self,canvas):
        #track
        canvas.create_oval(self.x-self.size,
                           self.y-self.size,
                           self.x+self.size,
                           self.y+self.size)
        #handle
        x = self.x+self.size*math.cos(math.radians(self.header))
        y = self.y+self.size*math.sin(math.radians(self.header))
        canvas.create_oval(x-self.nodeSize,
                           y-self.nodeSize,
                           x+self.nodeSize,
                           y+self.nodeSize,fill = "black")
        
