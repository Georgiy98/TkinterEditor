from tkinter import *
class File:
    def __init__(self):
        self.root = Tk()
    def run(self):
        self.root.mainloop()
    def frame_to_tk(self,frame):
        print(frame)
        self.root = Tk()
        for i in frame.place_slaves():
            exec(i.name+"= type(i)(self.root)")
            for u in i.keys():
                exec("""if not %s[u] == i[u]:
    %s[u] = i[u]"""%(i.name,i.name))
            code="%s.place(x=%s,y=%s"%(i.name,i.place_info()["x"],i.place_info()["y"])
            if not i.place_info()["width"] == "":
                code+=",width=%s"%i.place_info()["width"]
            if not i.place_info()["height"] == "":
                code+=",height=%s"%i.place_info()["height"]
            code+=")"
            exec(code)
            exec("%s.name = '%s'"%(i.name,i.name))
    def frame_to_window(self,frame):
        for i in frame.place_slaves():
            try:
                self.root[i] = frame[i]
            except:
                print(i)
        self.root.geometry("%sx%s+%s+%s"%(frame["width"],frame["height"],0,0))
