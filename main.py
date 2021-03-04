import PySimpleGUI as psg
import random

from PySimpleGUI.PySimpleGUI import main

for i in range(7):
    DiceRoll = random.randint(1,6)

Main = [[psg.Text("test")],
        [psg.Text(DiceRoll)],
        [psg.Button("start")]]
    
window = psg.Window("main window",Main)
