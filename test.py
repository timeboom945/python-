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
        
        frame1 = Frame(window)
        frame1.pack()
        label = Label(frame1,text = "谁赢了")
        I_win_button = Button(frame1,text = "我大",command = self.press_I_win_button)
        He_win_button = Button(frame1,text = "他大",command = self.press_He_win_button)
        I_win_button.grid(row = 1,column = 1)
        He_win_button.grid(row = 1,column = 5)
        
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2,text = "请输入你赢的点数")
        self.ok_button = Button(frame2,text = "ok",state = "disabled",command = self.press_ok_button)
        self.point = StringVar()
        self.entry = Entry(frame2,state = "disabled",textvariable = self.point)
        label.grid(row = 1,column = 1)
        self.entry.grid(row = 1,column = 2)
        self.ok_button.grid(row = 1,column = 3)
        
        window.mainloop()
    def press_start_button(self):
        self.canvas.delete("all")
        a_random_point = row_a_number()
        px = random.randint(50,950)
        py = random.randint(50,600)
        obpx = 500
        obpy = 300
        tag_text = "pic1"
        picture = self.number_list[a_random_point - 1]
        self.canvas.create_image(px,py,image = picture,tags = tag_text)
        dx = (obpx - px) // 50
        dy = (obpy - py) // 50
        x = px
        y = py
        count = 0
        while True:
            if count % 5 != 0:
                self.canvas.move("pic1",dx,dy)
                x += dx
                y += dy
                self.canvas.after(5)
                self.canvas.update()   #重新显示画布
                count += 1
            else:
                random_num = random.randint(1,6)
                picture = self.number_list[random_num - 1]
                self.canvas.delete("pic1")
                x += dx
                y += dy
                self.canvas.create_image(x,y,image = picture,tags = "pic1")
                count += 1
                self.canvas.after(5)
            if count > 50:
                break
        a_random_point = row_a_number()
        px = random.randint(50,950)
        py = random.randint(50,600)
        obpx = 900
        obpy = 300
        tag_text = "pic2"
        picture = self.number_list[a_random_point - 1]
        self.canvas.create_image(px,py,image = picture,tags = tag_text)
        dx = (obpx - px) // 50
        dy = (obpy - py) // 50
        x = px
        y = py
        count = 0
        while True:
            if count % 5 != 0:
                self.canvas.move("pic2",dx,dy)
                x += dx
                y += dy
                self.canvas.after(5)
                self.canvas.update()
                count += 1
            else:
                random_num = random.randint(1,6)
                picture = self.number_list[random_num - 1]
                self.canvas.delete("pic2")
                x += dx
                y += dy
                self.canvas.create_image(x,y,image = picture,tags = "pic2")
                count += 1
                self.canvas.after(5)
            if count > 50:
                break
    def press_I_win_button(self):
        self.entry["state"] = "normal"
        self.ok_button["state"] = "normal"
    def press_He_win_button(self):
        if self.trial_count < 40:
            self.canvas.delete("pic")
            self.press_start_button()
            self.trial_count += 1
        else:
            self.canvas.delete("all")
            self.canvas.creat_text(960,450,"实验结束")
    def press_ok_button(self):
        self.trial_count += 1
        self.press_start_button()
        self.entry.delete(0,END)
        self.entry["state"] = "disabled"
        self.ok_button["state"] = "disabled"
test()