from tkinter import *
from tkinter.messagebox import *
from classes.SCROLL_FRAME import *
import os,os.path,create_new_project_window
def run(root,file):
    global way
    def act():
        create_new_project_window.get_way(way_label["text"],os.listdir(way+"\\"))
        window.destroy()
    def back():
        global way
        if ("\\" in way):
            way=way[:way.rindex('\\')]
            go()
    def new_folder():
        def create():
            try:
                global way
                os.mkdir(way+"\\"+name_folder.get())
                way+="\\"+name_folder.get()
                message.destroy()
                go()
                window.grab_set()
                window.focus_set()
            except:
                showerror("Creating folder..","Cannot create this folder in current directory!")
                message.grab_set()
                message.focus_set()
        message=Toplevel(window)
        message.config(bg="#777777")
        message.title("Новая папка")
        message.resizable(False,False)
        message.grab_set()
        message.focus_set()
        message.geometry("200x100+500+300")
        Label(message, text="ENTER NAME:",fg = "#99CC99",bg = "#555555",font = "Arial 10 bold").place(x=10,y=5)
        name_folder = Entry(message,width=30,fg = "#99CC99",bg = "#555555" )
        name_folder.place(x=10,y=30)
        Button(message,text = "Create",height=1,font="Arial 18 bold",width=12,fg = "#99CC99",bg = "#555555" ,command=create).place(x=10,y=50)
    def disk():
        folder_panel.place(x=20,y=5)
        way_panel.field.place(x=5000,y=5000)
        disk_but.place(x=5000,y=5000)
        back_but.place(x=5000,y=5000)
        choose_but.place(x=5000,y=5000)
        global way
        way=""
    def click(event):
        global way
        way+="\\"+event.widget["text"]
        go()
    def go():
        global way
        if (os.path.isdir(way)):
            for i in way_panel.field.place_slaves():
                if not i in way_panel.exception:
                    i.destroy()
            h=os.listdir(way+"\\")
            t=0
            for i in range(len(h)):
                if (os.path.isdir(way+"\\"+h[i]) or file):
                    i=Button(way_panel.field,text=h[i],width=61,font="Arial 7 bold")
                    i.bind("<1>",click)
                    i.place(x=5,y=5+25*t)
                    t+=1
            way_label["text"]=way
            new_folder_but = Button(way_panel.field,text="+",font="Arial 15 bold",width=1,height = 1, bg="#333366",fg="#DDDDBB",command=new_folder)
            new_folder_but.place(x=380,y=225)
            way_panel.add_exception(new_folder_but)
        else:
            showinfo("Tkinter Editor - Error", "This directory ( "+way+" ) doesn't exist!\nChoose real directory!")

    def choose_disk(event):
        global way
        way=event.widget["text"][5]+":"
        if (os.path.isdir(way)):
            way_panel.field.place(x=20,y=5)
            folder_panel.place(x=5000,y=5000)
            disk_but.place(x=0,y=0)
            back_but.place(x=0,y=150)
            choose_but.place(x=260,y=550)
            go()
        else:
             showinfo("Tkinter Editor - Error", "This directory ( "+way+" ) doesn't exist!\nChoose real directory!")

    def other():
        global way
        way=other_way.get()
        if (os.path.isdir(way)):
            way_panel.field.place(x=20,y=5)
            folder_panel.place(x=5000,y=5000)
            disk_but.place(x=0,y=0)
            back_but.place(x=0,y=150)
            choose_but.place(x=260,y=550)
            go()
        else:
            showinfo("Tkinter Editor - Error", "This directory ( "+way+" ) doesn't exist!\nChoose real directory!")

    way=""
    window=Toplevel(root)
    window.grab_set()
    window.focus_set()
    window.configure(bg="#222222")
    window.geometry("440x600+400+20")
    window.title("Tkinter Editor"+" "*20+"Explorer")
    way_panel=Scroll_frame(window,f_bg="#555555",f_width=400,f_height=490,f_x=20,f_y=5)
    way_panel.put()
    way_panel.create_yscroll(380,1,380,280,
                     up_b=Button(way_panel.field,text=(chr(708)+"\n")*7,font="Arial 15 bold",width=1,bg="#333366",fg="#DDDDBB"),
                     down_b=Button(way_panel.field,text=("\n"+chr(709))*7,font="Arial 15 bold",width=1,bg="#333366",fg="#DDDDBB"))
    way_label=Label(window,font="Arial 10 bold",fg="#99CC99",bg=window["bg"])
    way_label.place(x=20,y=510)
    new_folder_but = Button(way_panel.field,text="+",font="Arial 15 bold",width=1,height = 3, bg="#333366",fg="#DDDDBB")
    new_folder_but.place(x=380,y=240)
    #q=PhotoImage(file="images//home.gif")
    #Button(image=q).place(x=0,y=300)
    disk_but=Button(window,width=1,text="D\nA\nT\nA",font="Arial 15 bold",fg="#99CC99",bg=window["bg"],command=disk)
    back_but=Button(window,width=1,text=chr(706),font="Arial 15 bold",fg="#99CC99",bg=window["bg"],command=back)
    folder_panel=Frame(window,bg="#555555",width=400,height=500)
    folder_panel.place(x=20,y=5)
    for u in range(ord('A'),ord('M')):
        i=Button(folder_panel,text="Data "+chr(u),bg="#227722",font="Arial 25 bold",width=9)
        t=u-ord('A')
        i.place(x=200*(t%2),y=(t-t%2)*40)
        i.bind("<1>",choose_disk)
    other_way=Entry(folder_panel,bg="#449944",font="Arial 14",width=12)
    other_way.place(x=0,y=470)
    choose_but=Button(window,text="Choose",font="Arial 15 bold", fg="#CCCCCC", bg=window["bg"],relief=FLAT,command=act)
    Button(folder_panel,text="Choose another data/catalog",bg="#227722",font="Arial 10 bold",width=30,command=other).place(x=150,y=470)
    window.wait_window()
    window.mainloop()
