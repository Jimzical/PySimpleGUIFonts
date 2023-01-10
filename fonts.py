from tkinter import Tk, font
import  PySimpleGUI as sg
root = Tk()
font_tuple = font.families()
root.destroy()
#Creates a Empty list to hold font names
FontList=[]
for font in font_tuple:
    FontList.append(font)

lay = []
for font in FontList:
    lay.append([sg.Text(font, font=(font, 20))])
    print(font)
col = sg.Column(lay, scrollable=True, vertical_scroll_only=True)
layout = [[col]]
window = sg.Window("All fonts installed using PySimpleGUI", layout, grab_anywhere=True, resizable=True)
event, values = window.read()
