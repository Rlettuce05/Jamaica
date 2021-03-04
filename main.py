import PySimpleGUI as psg
import random

#from PySimpleGUI.PySimpleGUI import main

DiceRoll = []
for i in range(7) :
    DiceRoll.append(random.randint(1,6))

Main = [[psg.Text("this is test program")],
        [psg.Text(DiceRoll)],
        [psg.Button("start")]]
   
window = psg.Window("main window",Main,size=(500,500))

while True :
    event , values = window.read()
    if event in (None,"start") :
        break

window.close()