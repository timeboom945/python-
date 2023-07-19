from tkinter import *
from PIL import ImageTk
from PIL import Image
class demo:
    def __init__(self):
        window = Tk()
        window.title("image demo")
        
        one = PhotoImage(file = "image/one.gif")
        two = PhotoImage(file = "image/two.gif")
        three = PhotoImage(file = "image/three.gif")
        four = PhotoImage(file = "image/four.gif")
        five = PhotoImage(file = "image/five.gif")
        
        self.canvas = Canvas(window,bg = "white",width = 1400,height = 650)
        self.canvas.pack()
        
        angel = 0
        self.canvas.create_image(700,325,image = five,tags = "pic")
        while True:
            self.canvas.delete("pic")
            five = five.rotate(angel)
            self.canvas.create_image(700,325,image = five,tags = "pic")
            self.canvas.after(100)
            self.canvas.update()
            angle += 10
        
        window.mainloop()
demo()