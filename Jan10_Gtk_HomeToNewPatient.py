#!/usr/bin/env python3

import pgi
pgi.require_version("Gtk", "3.0")
from pgi.repository import Gtk
import csv

window_w = 700 # Window Width
window_h = 500 # Window Height

class HomeWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Home Window")
        Gtk.Window.set_default_size(self, window_w, window_h) # Set Default Window Size

        # FIGURE OUT MENUBAR STUFF...
        #menubar = Gtk.MenuBar
        #Gtk.Application.set_menubar(self, Gtk.MenuBar)

        self.box = Gtk.Box(spacing=6) # Box Layout Container
        self.add(self.box)
        # self.box.pack_start(menubar, True,True,0)

        self.testButton = Gtk.Button(label="Click Here")
        self.testButton.connect("clicked", self.on_testButton_clicked)
        self.box.pack_start(self.testButton,True,True,0)

        self.newPatButton = Gtk.Button(label="New Patient")
        self.newPatButton.connect("clicked",self.on_newPatButton_clicked)
        self.box.pack_start(self.newPatButton,True,True,0)


    def on_testButton_clicked(self, widget):
        print("Hello World")

    def on_newPatButton_clicked(self, widget):
        newPatWin = NewPatientWindow()
        newPatWin.show_all()



class NewPatientWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Patient Window")
        Gtk.Window.set_default_size(self, window_w, window_h) # Set Default Window Size

        self.grid = Gtk.Grid() # Grid Layout Container
        self.add(self.grid)

        self.firstNameLabel = Gtk.Label("First Name: ")
        self.firstNameEntry = Gtk.Entry()

        self.grid.add(self.firstNameLabel)
        self.grid.add(self.firstNameEntry)

        self.lastNameLabel = Gtk.Label("Last Name: ")
        self.lastNameEntry = Gtk.Entry()

        self.grid.add(self.lastNameLabel)
        self.grid.add(self.lastNameEntry)


        self.submitButton = Gtk.Button(label="Submit")
        self.submitButton.connect("clicked", self.on_submitButton_clicked)
        self.grid.add(self.submitButton)

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


#widget = Gtk.Box()
#print(dir(widget.props)) # LEARN WHAT PROPERTIES A WIDGET HAS!!!

win = HomeWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
