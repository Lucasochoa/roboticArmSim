#from MotorController import *
from HelperFunctions import *
import math

class Slider(object):
    def __init__(self,name,x,y,width,size,start,end):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.start = start
        self.end = end
        self.curX = x
        self.size = size
        self.active = False

    def mouseClickedDown(self,event):
        if self.distance(event.x,event.y,self.curX,self.y) < self.size:
            self.active = True
            return True
        return False

    def updateSlider(self,data):
        if data.selectedLimb != None: 
            tempLimb = data.selectedLimb
            if self.name == "rotation":
                self.curX =self.x+ translate(math.degrees(tempLimb.rotation),\
                0,360,0,150)%150
            elif self.name == "speed":
                self.curX = self.x + translate(tempLimb.speed,0,50,0,150)
            elif self.name == "length":
                self.curX = self.x + translate(tempLimb.stemSize,6,20,0,150)
            

    def updateMenuSliders(self,data):
        tempEvent = data.EventMenu.selectedEvent
        if tempEvent != None:
            if self.name == "Event Speed":
                self.curX = self.x + translate(tempEvent.speed,0,50,0,100)
            elif self.name == "Event Duration":
                self.curX == self.x + translate(tempEvent.duration,0,100,0,100)
        else:
            self.curX = self.x


    def mouseMoved(self,event,data):

        if event.x >= self.x and event.x <=self.x+self.width and self.active:
            self.curX = event.x
            if data.selectedLimb != None:
                #print(translate(event.x,self.x,self.x+self.width,0,360))
                if self.name == "rotation":
                    data.selectedLimb.rotation = \
                    math.radians(translate(event.x,self.x,\
                        self.x+self.width,0,360))
                elif self.name == "speed":
                    data.selectedLimb.speed = \
                    translate(event.x,self.x,self.x+self.width,0,50)
                elif self.name == "length":
                    data.selectedLimb.stemSize = translate(event.x,self.x,
                        self.x+self.width,6,20)
                elif self.name == "Event Speed":
                    data.EventMenu.selectedEvent.speed = translate(event.x,
                        self.x,self.x+self.width,0,50)
                elif self.name == "Event Duration":
                    data.EventMenu.selectedEvent.duration = \
                    int(translate(event.x,self.x,self.x+self.width,0,100))
                    data.selectedLimb.updateEvents()

    def mouseReleased(self,event):
        self.active = False


    def draw(self,canvas,data):
        outputText = self.name
        if self.name == "Event Duration":
            if data.EventMenu.selectedEvent != None:
                outputText = self.name + ": "+\
                str(data.EventMenu.selectedEvent.duration)

        if self.name == "Event Speed":
            if data.EventMenu != None:
                outputText = self.name + ": "+\
                str(int(data.EventMenu.selectedEvent.speed))

        canvas.create_text(self.x, self.y-self.size,text=outputText,
                      fill="black", font="Helvetica 14")

        canvas.create_line(self.x,self.y,self.x+self.width,self.y)

        canvas.create_oval(self.curX-self.size/2,self.y-self.size/2,
                            self.curX+self.size/2,self.y+self.size/2,
                            fill ='black')      
    def distance(self,x,y,x2,y2):
        return ((x2-x)**2+(y2-y)**2)**.5                      
