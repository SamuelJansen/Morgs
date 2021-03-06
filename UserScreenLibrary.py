
import tkinter as tk
#from tkinter import ttk
from tkinter import *
import re
import pygame as pg
from PIL import ImageTk,Image
from sys import * #sys
from os import * #os


class UserScreen(tk.Tk):
    """ Transparent Tkinter Window Class. """

    def __init__(self,name,windowSize,status=False,x=0,y=0):
        #self.time = time

        tk.Tk.__init__(self)

        self.title(name)

        self.Drag = Drag(self)

        # Sets focus to the window.
        self.focus_force()

        # Removes the native window boarder.
        self.overrideredirect(True)

        # Disables resizing of the widget.
        self.resizable(False, False)

        # Places window above all other windows in the window stack.
        self.wm_attributes("-topmost", True)

        # This changes the alpha value (How transparent the window should be).
        # It ranges from 0.0 (completely transparent) to 1.0 (completely opaque).
        self.attributes("-alpha", 0.35)
        ###- print(self.winfo_height(),self.winfo_width())

        # The windows overall position on the screen
        self.size = windowSize
        self.wm_geometry( self.size + '+' + str(x) + '+' + str(y) )
        ###- self.wm_geometry(windowSize+'+' + str(0) + '+' + str(0))

        # Changes the window's color.
        # Check avaliable collors in Encycolorpedia:  https://encycolorpedia.com/html
        # For more specific search, use this: https://encycolorpedia.com/3e4134
        bg = '#000' #'#eb0d00' #'#ee0028'

        self.config(bg=bg)

        self.Frame = tk.Frame(self, bg=bg)

        # Exits the application when the window is right clicked.
        self.Frame.bind('<Button-3>', self.exit)

        # Changes the window's size indirectly.
        self.Frame.configure(width=600,height=900)

        """
        font = 'TextFonts/good_times_rg.ttf'
        size = 12

        cardText = open('CardText/CardText.txt', "r", encoding='utf-8')
        linesCardText = cardText.readlines()
        for line,l in zip(linesCardText,range(len(linesCardText))) :
            line = line.rstrip()
            if line.startswith('*') :
                label = tk.Label(self,text=line[2:],background=bg,foreground='white',font=font+' '+str(size)+' bold')
                label.pack()
            else :
                label = tk.Label(self,text=line,background=bg,foreground='white',font=font+' '+str(int(size*.75)))
                label.pack()
        cardText.close()
        #"""
        def callback():
            variables = {} #add a variable with witch execfile can return
            execfile('QuarterScreen.py')#,variables)
        b = tk.Button(self,text="OK",command=callback)
        b.pack()
        self.Frame.pack()


    def updatePosition(self,x=0,y=0):
        self.wm_geometry(self.size + '+' + str(x) + '+' + str(y))

    def exit(self, event):
        self.destroy()

    def position(self):
        _filter = re.compile(r"(\d+)?x?(\d+)?([+-])(\d+)([+-])(\d+)")
        pos = self.winfo_geometry()
        filtered = _filter.search(pos)
        self.X = int(filtered.group(4))
        self.Y = int(filtered.group(6))

        return self.X, self.Y

class Drag:
    """ Makes a window dragable. """

    def __init__(self, par, dissable=None, releasecmd=None):
        self.Par        = par
        self.Dissable   = dissable
        self.ReleaseCMD = releasecmd

        self.Par.bind('<Button-1>', self.relative_position)
        self.Par.bind('<ButtonRelease-1>', self.drag_unbind)

    def relative_position(self, event):
        cx, cy = self.Par.winfo_pointerxy()
        x, y = self.Par.position()
        self.OriX = x
        self.OriY = y
        self.RelX = cx - x
        self.RelY = cy - y
        self.Par.bind('<Motion>', self.drag_wid)

    def drag_wid(self, event):
        cx, cy = self.Par.winfo_pointerxy()
        d = self.Dissable

        if d == 'x':
            x = self.OriX
            y = cy - self.RelY
        elif d == 'y':
            x = cx - self.RelX
            y = self.OriY
        else:
            x = cx - self.RelX
            y = cy - self.RelY

        if x < 0:
            x = 0
        if y < 0:
            y = 0

        self.Par.wm_geometry('+' + str(x) + '+' + str(y))

    def drag_unbind(self, event):
        self.Par.unbind('<Motion>')
        if self.ReleaseCMD != None:
            self.ReleaseCMD()

    def dissable(self):
        self.Par.unbind('<Button-1>')
        self.Par.unbind('<ButtonRelease-1>')
        self.Par.unbind('<Motion>')
