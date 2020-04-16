from tkinter import *
def find_name(text):
    text = text.split("\n")
    for i in text:
        if "Tk(" in i:
            text = i
            break
    t=text.find("Tk")
    while (text[t]!="=" or text[t]==" "):
        t-=1
    t-=1
    word=""
    while text[t]!=" " and t>-1:
        word = text[t]+word
        t-=1
    return word
def copywidget(frame_from, frame_to):
    special_words = ["nw","ne","sw","se","n","s","e","w","center","inside"]
    for child in frame_from.winfo_children():
        newwidget = type(child)(frame_to)
        newwidget.name=child.name
        for i in child.keys():
            newwidget[i]=child[i]
        newwidget.place()
        command = "newwidget.place("
        for key in child.place_info().keys():
            try:
                print(key)
                if not child.place_info()[key]==newwidget.place_info()[key]:
                    print(key)
                    command += str(key)+" = "+str(child.place_info()[key])+", "
            except:
                if child.place_info()[key]!="" and not key in ["in","inside"]:
                    command += str(key)+" = "+str(child.place_info()[key])+", "
        command = command[:-2]+")"
        for i in special_words:
            if (" "+i+"," in command) or (" "+i+")" in command):
                command = command.replace(i,"\""+i+"\"")
        exec(command)
        for i in child.events:
            newwidget.bind(i[0],i[1])
class Window:
    def __init__(self,file_name):
        self.name = file_name
    def update_by_text(self,text):
        self.name = find_name(text)
        if ".mainloop" in text:
            txt=text.replace(self.name+".mainloop()","")
        exec(txt+"\nself.root="+self.name)
    def start_by_frame(self,frame):
        self.root = Tk()
        self.root.x = frame.place_info()["x"]
        self.root.y = frame.place_info()["y"]
        self.root.width = frame["width"]
        self.root.height = frame["height"]
        if frame.place_info()["width"] !="":
            self.root.width = frame.place_info()["width"]
            self.root.height = frame.place_info()["height"]
        self.root.name = frame.name
        copywidget(frame, self.root)
        self.root.geometry("%sx%s+%s+%s"%(self.root.width, self.root.height,self.root.x,self.root.y))
        for i in frame.keys():
            try:
                self.root[i]=frame[i]
            except:
                pass
    def close_window(self):
        self.root.destroy()
    def get_text(self):
        ex = Tk()
        text="from tkinter import *\n"+self.root.name+" = Tk()\n"
        text+= "root.geometry(\""+"%sx%s+%s+%s"%(self.root.width, self.root.height,self.root.x,self.root.y)+"\")\n"
        for u in self.root.keys():
            t = "\""*int(type(self.root[u]) == type(" "))
            if (ex[u]!=self.root[u] and not u in ["width","height"]):
                text+=self.root.name+"[\""+str(u)+"\"]="+t+str(self.root[u])+t+"\n"
        for i in self.root.place_slaves():
            example=type(i)(ex)
            example.place(x=-6000,y=-6000)
            text += i.name + "= "+str(type(i))[16:-2]+"("+self.root.name+")\n"
            for u in i.keys():
                t = "\""*int(type(i[u]) == type(" "))
                if example[u]!=i[u]:
                    text+=i.name+"[\""+str(u)+"\"]="+t+str(i[u])+t+"\n"
            text+=i.name+".place("
            for u in i.place_info().keys():
                if example.place_info()[u]!=i.place_info()[u] and not u in ["in"] :
                    text+=str(u)+"="+str(i.place_info()[u])+","
            text=text[:-1]+")\n"
        text+=self.root.name+".mainloop()"
        print(text)
        self.text = text
        ex.destroy()
        return text
