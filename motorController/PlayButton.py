from HelperFunctions import *
from Button import *

class PlayButton(Button):
    def __init__(self,name,x,y,width,height):
        super().__init__(name,x,y,width,height)

    def draw(self,canvas):
        round_rectangle(self.x,self.y,
            self.x+self.width,self.y+self.height,canvas, radius=30, fill="grey")
        canvas.create_polygon(self.x + self.width/3,self.y+self.height/4,
                                self.x + self.width/3,self.y+self.height*(3/4),
                                self.x+self.width*(2/3),self.y+self.height*.5)
