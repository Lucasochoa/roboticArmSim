from HelperFunctions import *
from Button import *
import math 


class LimbButton(Button):
    def __init__(self,name,x,y,width,height):
        super().__init__(name,x,y,width,height)

    def draw(self,canvas):
        round_rectangle(self.x,self.y,
            self.x+self.width,self.y+self.height,canvas, radius=30, fill="grey")
        self.drawLimbIcon(canvas,self.x+self.width//1.5,
            self.y+self.height//4,self.width//10)   


    def drawLimbIcon(self,canvas,x,y,size):
        rotation = math.degrees(45)
        #bottom bracket
        canvas.create_oval(x-size,
                           y-size,
                           x+size,
                           y+size)
        #middle tube
        canvas.create_line(x+size*math.cos(rotation),
                           y+size*math.sin(rotation),
                           x+size*5*math.cos(rotation),
                           y+size*5*math.sin(rotation))
        #end bracket
        x2 = x+size*6*math.cos(rotation)
        y2 = y+size*6*math.sin(rotation)
        canvas.create_oval(x2-size,
                           y2-size,
                           x2+size,
                           y2+size)
    def mouseRemoved(self,event,data):
      if super().clicked(event,data):
        data.tree.pop()
        data.selectedLimb = None
