from tkinter import *
from HelperFunctions import *
import math
import string

class Joint(object):
    def __init__(self,name,x,y,data):
        self.name = name
        self.x = x
        self.y = y
        self.x2,self.y2 = 0,0
        self.size = data.width//100
        self.rotation = math.radians(270)
        self.children = []
        self.parent = None
        self.speed = 5
        self.direction = 1
        self.stemSize = 5
        self.eventTime = 0
        self.events = []

    def __repr__(self):
        return __class__.__name__ +self.name +' '+str(self.x) + str(self.y)

    #distance formula
    def distance(self,x,y,x2,y2):
        return ((x2-x)**2+(y2-y)**2)**.5

    def clicked(self,event,data):
        #print('x: ', event.x , 'y: ',event.y)
        x = self.x + self.size*3
        y = self.y -self.size*3

        refreshInBounds = distance(x,y,event.x,event.y) < self.size
        # refreshInBounds = event.x > x-self.size and event.x <x+self.size and\
        #     event.y > y-self.size and event.y < y+self.size

        if data.selectedLimb != None:
            if data.selectedLimb == self and refreshInBounds:
                self.direction *= -1
                return self

        inbounds = self.distance(event.x,event.y,self.x,self.y)<self.size
        if inbounds:
            return self
        
        else: return None

    #check if clicked on end node
    def endNodeClicked(self,event,data):
        if (self.distance(self.x2,self.y2,event.x,event.y)<self.size):
            #print("apple")
            return self
        else: return None
       
    def playEvents(self):
        self.eventTime += 1
        if len(self.events) > 0:
            #check condition for for loop
            someEventHappened = False
            for event in self.events:
                if event.runEvent(self,self.eventTime):
                    someEventHappened = True
                    #print(self.eventTime,event.name)

            if not someEventHappened:
                self.eventTime = 0
        else:
            #limb.rotate(limb.speed*limb.direction)
            self.rotate(self.speed*self.direction)

    def addEvent(self,event):
        self.events.append(event)
        self.updateEvents()
        #if len(self.events) != 0:
        # if len(self.events) == 0:
        #     self.events.append(event)
        # else:
        #     #updates to be after previous event
        #     event.startTime = self.events[len(self.events)-1].duration +
        #     event.duration = event.duration + event.startTime
        #     self.events.append(event)

    # def updateEvents(self,depth):
    #     if depth

    def updateEvents(self):
        print("working")
        for i in range(len(self.events)):
            tempEvent = self.events[i]
            if i == 0:
                tempEvent.startTime = 0
            else:
                prevEvent = self.events[i-1]
                tempEvent.startTime = prevEvent.startTime + prevEvent.duration



    def setRotation(self,rotation):
        self.rotation = rotation

    def rotate(self,amount):
        self.rotation += math.radians(amount)

    def setChild(self,child):
        self.children.append(child)
        child.setParent(self)

    def setParent(self,parent):
        self.parent = parent

    def updateChildren(self):
        for child in self.children:
            child.update()

    def update(self):
        #check if has parent to avoid crash
        if self.parent != None:
            self.x = self.parent.x2
            self.y = self.parent.y2

    def drawArrowsForRotation(self,canvas,x,y):

        padding = self.size/6
        canvas.create_polygon(x-self.size*1.75-padding,
            self.y+self.size/2+padding,
            x-self.size*2.4-padding, y-self.size+padding,
            x-self.size-padding, y-self.size+padding,fill = "blue")

    def drawRotationDial(self,canvas,data):
        canvas.create_image(self.x+self.size*2,self.y-self.size*4, anchor=NW,
         image=data.loadIconImages["refresh"])

        canvas.create_arc([self.x-self.size*2,self.y-self.size*2,
                                self.x+self.size*2,self.y+self.size*2],
                                style =ARC,
                                start =0,
                                extent = 180,#math.radians(math.pi),
                                width = self.size/3 , outline = "blue")
    
        if self.direction == -1:
            self.drawArrowsForRotation(canvas,self.x,self.y)
        else:
            self.drawArrowsForRotation(canvas,self.x+self.size*3.8,self.y)

        # canvas.create_line(self.x-self.size*2,self.y,self.x-self.size*2,
        #     self.y-self.size,width = self.size/3, fill = "blue")
        # canvas.create_line(self.x-self.size*2,self.y,self.x-self.size*1.5,
        #     self.y-self.size,width = self.size/3,fill = "blue")

    def drawLimmitDial(self,canvas,data):
        canvas.create_arc([self.x-self.size*2,self.y-self.size*2,
                                self.x+self.size*2,self.y+self.size*2],
                                style =ARC,
                                start =0,
                                extent = math.degrees(self.rotation+20),
                                width = self.size/3 , outline = "blue")

    def draw(self,canvas):
        #bottom bracket
        canvas.create_oval(self.x-self.size,
                           self.y-self.size,
                           self.x+self.size,
                           self.y+self.size)
        #middle tube
        canvas.create_line(self.x+self.size*math.cos(self.rotation),
                           self.y+self.size*math.sin(self.rotation),
                           self.x+self.size*self.stemSize*math.cos(self.rotation),
                           self.y+self.size*self.stemSize*math.sin(self.rotation))

        #end bracket
        #should i be updating
        self.x2 = self.x+self.size*(self.stemSize+1)*math.cos(self.rotation)
        self.y2 = self.y+self.size*(self.stemSize+1)*math.sin(self.rotation)
        canvas.create_oval(self.x2-self.size,
                           self.y2-self.size,
                           self.x2+self.size,
                           self.y2+self.size)
