from tkinter import*
import math
class Color_widget:
    def __init__(self,root):
        self.field = Frame(root,width=53,height = 22,bg="#FFFF00")
        t=Button(self.field,bg="#FF0000",fg="white",text="+",relief = "flat",font="Arial 10 bold")
        t.bind("<1>",self.change_color)
        t.place(x=0,y=0,width=10,height=10)
        t=Button(self.field,bg="#FF0000",fg="white",text="-",relief = "flat",font="Arial 10 bold")
        t.bind("<1>",self.change_color)
        t.place(x=0,y=11,width=10,height=10)
        t=Button(self.field,bg="#00FF00",fg="white",text="+",relief = "flat",font="Arial 10 bold")
        t.bind("<1>",self.change_color)
        t.place(x=11,y=0,width=10,height=10)
        t=Button(self.field,bg="#00FF00",fg="white",text="-",relief = "flat",font="Arial 10 bold")
        t.bind("<1>",self.change_color)
        t.place(x=11,y=11,width=10,height=10)
        t=Button(self.field,bg="#0000FF",fg="white",text="+",relief = "flat",font="Arial 10 bold")
        t.bind("<1>",self.change_color)
        t.place(x=22,y=0,width=10,height=10)
        t=Button(self.field,bg="#0000FF",fg="white",text="-",relief = "flat",font="Arial 10 bold")
        t.bind("<1>",self.change_color)
        t.place(x=22,y=11,width=10,height=10)
        self.img = Button(self.field,bg="#000000",fg="white",text="+",relief = "flat",command = self.ch_color_wind)
        self.img.place(x=33,y=0,width=20,height=23)

    def ch_c(self,val,event):
        if event.widget["text"] == "+":
            val+=1
        else:
            val-=1
        if val<0:
            val=0
        elif val > 255:
            val=255
        return val
    def use_sec_clr(self,event):
        t=event.widget["bg"]
        self.lb_cl["bg"] = t
        self.r_bar.set(int(t[1:3],16))
        self.g_bar.set(int(t[3:5],16))
        self.b_bar.set(int(t[5:],16))
    def change_color(self,event):
        first_val = self.img["bg"]
        red = int(first_val[1:3],16)
        green=int(first_val[3:5],16)
        blue =int(first_val[5:],16)
        rgb=[blue,green,red]
        exec('rgb[int(math.log(int(event.widget["bg"][1:],16),256))]'+event.widget["text"]+"=5")
        if rgb[int(math.log(int(event.widget["bg"][1:],16),256))]>255:
            rgb[int(math.log(int(event.widget["bg"][1:],16),256))]=255
        if rgb[int(math.log(int(event.widget["bg"][1:],16),256))]<0:
            rgb[int(math.log(int(event.widget["bg"][1:],16),256))]=0
        t=hex(rgb[2]*256*256+rgb[1]*256+rgb[0])[2:]
        t="#"+"0"*(6-len(t))+t
        self.img["bg"] = t

    def place(self,x,y):
        self.field.place(x=x,y=y)
    def get(self):
        return self.img["bg"]
    def apply(self):
        clr = self.r_bar.get()*256*256+self.g_bar.get()*256+self.b_bar.get()
        clr=hex(clr)[2:]
        clr="#"+"0"*(6-len(clr))+clr
        self.lb_cl["bg"] = clr
        self.ch_sec_cl()
    def ch_sec_cl(self):
        t=int(self.lb_cl["bg"][1:],16)
        r = int(self.lb_cl["bg"][1:3],16)
        g = int(self.lb_cl["bg"][3:5],16)
        b = int(self.lb_cl["bg"][5:],16)
        for i in range(len(self.g_l)):
            if ((r+i-30)>0 and  (r+i-30)<255):
                q=t+(i-30)*255*255
                q=hex(q)[2:]
                print(q)
                q="#"+"0"*(6-len(q))+q
                print(q)
                self.r_l[i]["bg"] = q
            else:
                self.r_l[i]["bg"] = "white"

        r = int(self.lb_cl["bg"][1:3],16)
        g = int(self.lb_cl["bg"][3:5],16)
        b = int(self.lb_cl["bg"][5:],16)

        for i in range(len(self.g_l)):
            if ((g+i-30)>0 and  (g+i-30)<255):
                q=t+(i-30)*255
                q=hex(q)[2:]
                q="#"+"0"*(6-len(q))+q
                self.g_l[i]["bg"] = q
            else:
                self.g_l[i]["bg"] = "white"

        r = int(self.lb_cl["bg"][1:3],16)
        g = int(self.lb_cl["bg"][3:5],16)
        b = int(self.lb_cl["bg"][5:],16)

        for i in range(len(self.g_l)):
            if ((b+i-30)>0 and  (b+i-30)<255):
                q=t+i-30
                q=hex(q)[2:]
                q="#"+"0"*(6-len(q))+q
                self.b_l[i]["bg"] = q
            else:
                self.b_l[i]["bg"] = "white"

    def ok(self):
        self.img["bg"] = self.lb_cl["bg"]
        self.clr_dialog.destroy()
    def ch_color_wind(self):
        self.clr_dialog = Toplevel(self.field.master,bg = "white")
        self.clr_dialog.state("zoomed")
        Label(self.clr_dialog,text = "RED",font = "Arial 20 bold",fg = "red").place(x=40,y=10)
        self.r_bar = Scale(self.clr_dialog,orient="horizontal",to=255,bg = "red", fg = "white", font = "Arial 10 bold")
        self.r_bar.place(x=20,y=40)
        Label(self.clr_dialog,text = "GREEN",font = "Arial 20 bold",fg = "green").place(x=170,y=10)
        self.g_bar = Scale(self.clr_dialog,orient="horizontal",to=255,bg = "green", fg = "white", font = "Arial 10 bold")
        self.g_bar.place(x=170,y=40)
        Label(self.clr_dialog,text = "BLUE",font = "Arial 20 bold",fg = "blue").place(x=330,y=10)
        self.b_bar = Scale(self.clr_dialog,orient="horizontal",to=255,bg = "blue", fg = "white", font = "Arial 10 bold")
        self.b_bar.place(x=320,y=40)
        Button(self.clr_dialog, text = "apply",command = self.apply).place(x=20,y=80)
        self.lb_cl = Label(self.clr_dialog, bg="#000000")
        self.lb_cl.place(x=20,y=100,width = 300,height=50)
        self.r_l = []
        self.g_l = []
        self.b_l = []
        for i in range(61):
            self.r_l.append(Label(self.clr_dialog))
            self.r_l[i].place(x=20,y=170+5*i,width=100,height=5)
            self.r_l[i].bind("<1>",self.use_sec_clr)
            self.g_l.append(Label(self.clr_dialog))
            self.g_l[i].place(x=170,y=170+5*i,width=100,height=5)
            self.g_l[i].bind("<1>",self.use_sec_clr)
            self.b_l.append(Label(self.clr_dialog))
            self.b_l[i].place(x=320,y=170+5*i,width=100,height=5)
            self.b_l[i].bind("<1>",self.use_sec_clr)
        self.ch_sec_cl()
        Button(self.clr_dialog,text = "OK",command = self.ok).place(x=20,y=480)
