from tkinter import *
import time
import random

def row_a_number():
    return random.randint(1,6)

class test:
    def __init__(self):
        window = Tk()
        window.title("image demo")
        
        one = PhotoImage(file = "image/one.gif")
        two = PhotoImage(file = "image/two.gif")
        three = PhotoImage(file = "image/three.gif")
        four = PhotoImage(file = "image/four.gif")
        five = PhotoImage(file = "image/five.gif")
        six = PhotoImage(file = "image/six.gif")
        
        self.number_list = [one,two,three,four,five,six]
        
        self.canvas = Canvas(window,bg = "white",width = 1400,height = 650)
        self.canvas.pack()
        
        self.trial_count = 0
        
        frame0 = Frame(window)
        frame0.pack()
        start_button = Button(frame0,text = "开始",command = self.press_start_button)
        start_button.pack()

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2,text = "请输入骰子的个数")
        self.ok_button = Button(frame2,text = "ok",command = self.press_ok_button)
        self.point = StringVar(value = 1)
        self.entry = Entry(frame2,textvariable = self.point)
        label.grid(row = 1,column = 1)
        self.entry.grid(row = 1,column = 2)
        self.ok_button.grid(row = 1,column = 3)
        
        window.mainloop()
    def press_start_button(self):
        self.canvas.delete("all")
        for i in range(eval(self.point.get())):
            a_random_point = row_a_number()
            px = random.randint(50,950)
            py = random.randint(50,600)
            obpx = random.randint(50,950)
            obpy = random.randint(50,600)
            tag_text = "pic" + str(i + 1)
            picture = self.number_list[a_random_point - 1]
            self.canvas.create_image(px,py,image = picture,tags = tag_text)
            h = round(((obpx - px) ** 2 + (obpy - py) ** 2) ** 0.5,2)
            cosx = round((obpx - px) / h,2)
            cosy = round((obpy - py) / h,2)
            u = round((2 * h) / (((0.25) ** 2) * 980),2)
            x = px
            y = py
            count = 0
            t = 0.25
            while True:
                if count % 5 != 0:
                    v0 = round(980 * u * t,2)
                    dx = round(cosx * v0 * 0.005,2)
                    dy = round(cosy * v0 * 0.005,2)
                    self.canvas.move(tag_text,dx,dy)
                    x += dx
                    y += dy
                    self.canvas.after(5)
                    t -= 0.005
                    self.canvas.update()   #重新显示画布
                    count += 1
                else:
                    random_num = random.randint(1,6)
                    picture = self.number_list[random_num - 1]
                    self.canvas.delete(tag_text)
                    v0 = round(980 * u * t,2)
                    dx = round(cosx * v0 * 0.005,2)
                    dy = round(cosy * v0 * 0.005,2)
                    x += dx
                    y += dy
                    self.canvas.create_image(x,y,image = picture,tags = tag_text)
                    count += 1
                    self.canvas.after(5)
                    t -= 0.005
                if count > 50:
                    break
    def press_ok_button(self):
        self.press_start_button()
test()