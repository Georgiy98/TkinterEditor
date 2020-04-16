with open("settings.txt","r") as f:
    lang = f.read()
attributes = dict()
with open("languages//attr_"+lang[:-1]+".txt") as f:
    for i in f.readlines()[:-1]:
        attributes[i.split("=")[0]] = i.split("=")[1][:-1]
"""from tkinter import *
for i in Button().keys():
    print(i+"=")"""
