from HelperFunctions import *
from Button import *

class AddEventButton(Button):
    def __init__(self,name,x,y,width,height):
        super().__init__(name,x,y,width,height)

    def draw(self,canvas,data):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,
            self.y + self.height, fill = 'grey',width =2)

        canvas.create_line(self.x+self.width/2,self.y+self.height/5,
                           self.x+self.width/2,self.y+self.height*(4/5))
        canvas.create_line(self.x+self.width/5,self.y+self.height/2,
                           self.x+self.width*(4/5),self.y+self.height/2)

class AddRotationEventButton(Button):
    def __init__(self,name,x,y,width,height):
        super().__init__(name,x,y,width,height)

    def draw(self,canvas,data):
        round_rectangle(self.x,self.y,
            self.x+self.width,self.y+self.height,canvas,radius=30,fill="grey")
        canvas.create_text(self.x+self.width/2,self.y+self.height/2,
                text=self.name,fill="black",
                font="Helvetica 16 bold")

