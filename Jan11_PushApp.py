#!/usr/bin/env python3

import pgi
pgi.require_version("Gtk", "3.0")
from pgi.repository import Gtk, Gdk, GdkPixbuf
import csv
from matplotlib.figure import Figure
import numpy as np

#from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Cairo as FigureCanvas

# TO GET MATPLOT LIB EMBEDDED IN GTK3
# from matplotlib.backends.backend_gtk3agg import (
#     FigureCanvasGTK3Agg as FigureCanvas)

window_w = 700 # Window Width
window_h = 500 # Window Height

class HomeWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Home Window")
        Gtk.Window.set_default_size(self, window_w, window_h) # Set Default Window Size


        # FIGURE OUT MENUBAR STUFF...
        # mb = Gtk.MenuBar(Gtk.Window)
        #
        # homeMenuBar = Gtk.Menu()
        # fileMenu = Gtk.MenuItem("_File")
        # fileMenu.set_submenu(homeMenuBar)

        #newPatMenuBar = Gtk.MenuItem("New Patient")
        #homeMenuBar.append(newPatMenuBar)
        #fileMenu.append(newPatMenuBar)

        #openMenuBar = Gtk.MenuItem("Open...")
        #homeMenuBar.append(openMenuBar)
        #fileMenu.append(openMenuBar)

        #endSeshMenuBar = Gtk.MenuItem("End Session")
        #homeMenuBar.append(endSeshMenuBar)
        #fileMenu.append(endSeshMenuBar)

        # mb.append(fileMenu)

        #Gtk.Application.set_menubar(self, Gtk.MenuBar)

        box = Gtk.Box(spacing=6) # Box Layout Container
        self.add(box)
        # self.box.pack_start(menubar, True,True,0)

        aboutBox = Gtk.AboutDialog()
        #gtk_show_about_dialog()

        self.testButton = Gtk.Button(label="Click Here")
        self.testButton.connect("clicked", self.on_testButton_clicked)
        box.pack_start(self.testButton,True,True,0)

        self.newPatButton = Gtk.Button(label="New Patient")
        self.newPatButton.connect("clicked", self.on_newPatButton_clicked)
        #self.newPatButton.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(6400,6400,6440))
        box.pack_start(self.newPatButton,True,True,0)

    def on_testButton_clicked(self, widget):
        print("Hello World")

    def on_newPatButton_clicked(self, widget):
        newPatWin = NewPatientWindow()
        newPatWin.show_all()



class NewPatientWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Patient Window")
        Gtk.Window.set_default_size(self, window_w, window_h) # Set Default Window Size

        grid = Gtk.Grid() # Grid Layout Container
        self.add(grid)

        self.firstNameLabel = Gtk.Label("First Name: ")
        self.firstNameEntry = Gtk.Entry()

        grid.attach(self.firstNameLabel, 1, 1, 2, 2)
        grid.attach_next_to(self.firstNameEntry, self.firstNameLabel, 1, 2, 2)

        self.lastNameLabel = Gtk.Label("Last Name: ")
        self.lastNameEntry = Gtk.Entry()

        grid.attach_next_to(self.lastNameLabel,self.firstNameLabel, 3, 2, 2)
        grid.attach_next_to(self.lastNameEntry, self.lastNameLabel, 1, 2, 2)


        self.submitButton = Gtk.Button(label="Submit")
        self.submitButton.connect("clicked", self.on_submitButton_clicked)
        #grid.add(self.submitButton)
        grid.attach_next_to(self.submitButton, self.lastNameLabel, 3, 4, 2)

    def on_submitButton_clicked(self, widget):
        firstNameVar = self.firstNameEntry.get_text()
        lastNameVar = self.lastNameEntry.get_text()

        print(firstNameVar + ' ' + lastNameVar)
        currentPatientFileName = lastNameVar + "_" + firstNameVar + "_DateTime.csv"
        fullPatientFilePath = "PatientFiles/" + currentPatientFileName

        with open(fullPatientFilePath, mode="w") as curFile:
            # Names: time, left ischial spine, right ischial spine, pubic bone, sacral promontory, sacrum, fetal head
            headerNames = ['time', 'lIS', 'rIS', 'pb', 'sp', 's', 'fh']
            writer = csv.DictWriter(curFile, fieldnames=headerNames)

            writer.writeheader()

        subWin = InitialWindow()
        subWin.show_all()



class InitialWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="InitialWindow")
        Gtk.Window.set_default_size(self, window_w, window_h) # Set Default Window Size

        initGrid = Gtk.Grid()
        self.add(initGrid)

        momDisp = Gtk.Box()
        initGrid.add(momDisp)

        self.beginButton = Gtk.Button(label="Begin")
        self.beginButton.connect("clicked", self.on_beginButton_clicked)
        initGrid.add(self.beginButton)

        #pelvIm = Gtk.Image()
        #pelvIm.set_from_file("pelvisim.png")
        #pelvIm.new_from_file_at_scale("pelvisim.png",24,24,True)
        #pelvIm.set_pixel_size(10)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("pelvisim.png",100,100,True)
        pelvIm = Gtk.Image.new_from_pixbuf(pixbuf)
        initGrid.add(pelvIm)



    def on_beginButton_clicked(self, widget):
        print("Begin Button Clicked")




win = HomeWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
