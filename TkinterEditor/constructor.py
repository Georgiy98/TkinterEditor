import tkinter, widget_create_change, Read_File
from classes.SCROLL_FRAME import *
from sys import path
import public_data as p
from classes.Timer import *
# project vision frame
def run(root, way, pr_name, window):
    current_widget = None
    def choose(event):
        path.append(r"D:\projects\Tk_editor\projects")
        w = __import__(pr_name)
        # print(dir(w
        widget_create_change.create_widget(window, event.widget.target, v)
    def f_run_mode(event):
        widget_create_change.run_mode(event)
    panel = PanedWindow(root, width=root.winfo_screenwidth() - 265, height=root.winfo_screenheight(), sashwidth=6)
    panel.place(x=0, y=0)
    w = root.master.maxsize()[0]
    h = root.master.maxsize()[1]
    imaging = Scroll_frame(panel, root.winfo_screenwidth() - 265, 0, root.winfo_screenwidth() - 265, h / 2 - 30,
                           "#BDB76B")
    imaging.create_yscroll(imaging.field.winfo_reqwidth(), 2, imaging.field.winfo_reqwidth(),
                           root.winfo_screenheight() - 280,
                           Button(root, text=(chr(708) + "\n") * 5, font="Arial 11 bold", width=1, bg="#8B4513",
                                  fg="#FFD700"),
                           Button(root, text=("\n" + chr(709)) * 5, font="Arial 11 bold", width=1, bg="#8B4513",
                                  fg="#FFD700")
                           )
    imaging.create_xscroll(1, root.winfo_screenheight() - 170, imaging.field.winfo_reqwidth() - 277,
                           root.winfo_screenheight() - 170,
                           Button(imaging.field, text="< " * 5, font="Arial 11 bold", height=1, bg="#8B4513",
                                  fg="#FFD700"),
                           Button(imaging.field, text=" >" * 5, font="Arial 11 bold", height=1, bg="#8B4513",
                                  fg="#FFD700")
                           )
    # imaging.put()
    # work_area = Frame(panel,bg="blue")
    catalog = Scroll_frame(panel, 0, 0, 190, root.winfo_screenheight() - 140, "#BBBBDD")
    panel.add(catalog.field)
    panel.add(imaging.field)
    Read_File.run(way + "//__init__.py", pr_name + ".py")
    path.append("projects")
    w = __import__(pr_name)
    w.run(imaging.field)
    # print(work_area.place_slaves())
    v = w.names
    v["root"].name = "root"
    v["root"].need_to_move = True
    v["root"].need_to_size = True
    v["root"].timer_move=Timer(widget_create_change.h_move,0.01)
    v["root"].timer_size=Timer(widget_create_change.h_resize,0.01)
    v["root"].events = []
    v["root"].bind("<1>",widget_create_change.run_mode)
    for i in v["root"].place_slaves():
        for u in v.items():
            i.name = "var"
            if u[1]==i:
                i.name=u[0]
                break
        i.need_to_move = True
        i.need_to_size = True
        i.timer_move=Timer(widget_create_change.h_move,0.01)
        i.timer_size=Timer(widget_create_change.h_resize,0.01)
        i.events = []
        i.bind("<1>",widget_create_change.run_mode)
    v["root"].bind("<1>",f_run_mode)
    widget_create_change.create_widget(0,0,v)

    p.constructor_frame = v["root"]
    catalog.create_yscroll(170, 1, 170, root.winfo_screenheight() - 265,
                           Button(catalog.field, text=(chr(708) + "\n") * 5, font="Arial 11 bold", width=1,
                                  bg="#8888AA"),
                           Button(catalog.field, text=("\n" + chr(709)) * 5, font="Arial 11 bold", width=1,
                                  bg="#8888AA"))

    Label(catalog.field, width=13, font="Arial 15 bold", bg="#BBBBDD", text="Standart:", anchor="w").place(x=0, y=0)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Button", anchor="e")
    h.target = Button(panel, width=6, text="Button")
    h.place(x=0, y=450)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Entry", anchor="e")
    h.target = Entry(panel, text="Ввод")
    h.place(x=0, y=30)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Text", anchor="e")
    h.target = Text(panel)
    h.place(x=0, y=60)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Label", anchor="e")
    h.target = Label(panel, text="Надпись")
    h.place(x=0, y=90)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Canvas", anchor="e")
    h.target = Canvas(panel)
    h.place(x=0, y=120)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Frame", anchor="e")
    h.target = Frame(panel, width=200, height=200)
    h.place(x=0, y=150)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="LabelFrame", anchor="e")
    h.target = LabelFrame(panel, width=200, height=100)
    h.place(x=0, y=180)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Listbox", anchor="e")
    h.target = Listbox(panel)
    h.place(x=0, y=210)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Message", anchor="e")
    h.target = Message(catalog.field)
    h.place(x=0, y=240)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Menu", anchor="e")
    h.target = Menu(catalog.field)
    h.place(x=0, y=270)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="PanedWindow", anchor="e")
    h.target = PanedWindow(catalog.field, width=200, height=100)
    h.place(x=0, y=300)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Radiobutton", anchor="e")
    h.target = Radiobutton(catalog.field)
    h.place(x=0, y=330)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Scale", anchor="e")
    h.target = Scale(catalog.field)
    h.place(x=0, y=360)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Scrollbar", anchor="e")
    h.target = Scrollbar(catalog.field)
    h.place(x=0, y=390)
    h.bind("<1>", choose)
    h = Button(catalog.field, width=20, font="Arial 10 bold", bg="#AAAACC", text="Spinbox", anchor="e")
    h.target = Spinbox(catalog.field)
    h.place(x=0, y=420)
    h.bind("<1>", choose)
    # for i in dir(tkinter):
    #    print(i)
