#!/usr/bin/env python3

import pgi
pgi.require_version("Gtk", "3.0")
from pgi.repository import Gtk, Gdk, GdkPixbuf
import csv
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime

#from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Cairo as FigureCanvas

# TODO: GET MATPLOT LIB EMBEDDED IN GTK3 TO PLOT SHIT
# from matplotlib.backends.backend_gtk3agg import (
#     FigureCanvasGTK3Agg as FigureCanvas)

#TODO: FIGURE OUT WINDOW TOGGLING STUFF

window_w = 1000 # Window Width
window_h = 500 # Window Height

# Application class contains all windows to toggle
class Application(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Home Window")
        Gtk.Window.set_default_size(self, window_w, window_h) # Set Default Window Size
        self.homeWindow(Gtk.Window) # Initial window is home...

    def homeWindow(self, widget):
        """
        """
        self.homeGrid = Gtk.Grid() # VBox container for label and for buttons
        self.add(self.homeGrid)

        self.labelGrid = Gtk.Grid() # Grid for label container
        self.homePageLabel = Gtk.Label("PUSH ASSIST HOME PAGE")

        self.labelGrid.add(self.homePageLabel)
        self.homeGrid.add(self.labelGrid)

        self.labelGrid.props.halign = Gtk.Align.CENTER # Align center
        self.labelGrid.props.valign = Gtk.Align.END # Align Center

        homeButtonGrid = Gtk.Grid() # Grid layout container for buttons
        self.homeGrid.add(homeButtonGrid) # Add to Vbox container

        homeButtonGrid.props.halign = Gtk.Align.CENTER # Align center
        homeButtonGrid.props.valign = Gtk.Align.END # Align botton

        self.openButton = Gtk.Button("Open...") # Open button... will lead to file selector for past patient files
        self.openButton.connect("clicked", self.on_openButton_clicked) # Open button action...
        homeButtonGrid.attach(self.openButton, 1,1,2,2) # Open button's layout

        self.newPatButton = Gtk.Button("New Patient") # New patient button leads to new patient window screen
        self.newPatButton.connect("clicked", self.on_newPatButton_clicked) # New patient button action...
        homeButtonGrid.attach_next_to(self.newPatButton, self.openButton, 1, 2, 2) #left=0, r=1, t=2, b=3

        self.backButton = Gtk.Button("Back") # Back button
        self.backButton.connect("clicked", self.on_backButton_clicked) # Back button action
        homeButtonGrid.attach_next_to(self.backButton, self.newPatButton, 1, 1, 1) # Back button layout

    def on_openButton_clicked(self, widget):
        """
        """
        # TODO: Actually have a file selecting window pop up here
        print("Open... Button")

    def on_newPatButton_clicked(self, widget):
        """
        """
        #newPatWin = NewPatientWindow()
        #newPatWin.show_all()
        print("New Patient Window")
        self.labelGrid.remove(self.homePageLabel)
        self.fakeButton = Gtk.Button("TESTING")
        self.labelGrid.add(self.fakeButton)
        #self.newPatWin(Gtk.Window)

    def on_backButton_clicked(self, widget):
        """
        """
        print("Back")
        self.labelGrid.add(self.homePageLabel)

    def newPatWin(self, widget):
        """
        """
        self.patGrid = Gtk.Grid() # Grid Layout Container
        self.homeGrid.add(self.patGrid)
        patGrid.props.valign = Gtk.Align.CENTER
        patGrid.props.halign = Gtk.Align.CENTER

        self.firstNameLabel = Gtk.Label("First Name: ")
        self.firstNameEntry = Gtk.Entry()

        patGrid.attach(self.firstNameLabel, 1, 1, 2, 2)
        patGrid.attach_next_to(self.firstNameEntry, self.firstNameLabel, 1, 2, 2) #left=0, r=1, t=2, b=3


class NewPatientWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Patient Window")
        Gtk.Window.set_default_size(self, window_w, window_h) # Set Default Window Size

        patGrid = Gtk.Grid() # Grid Layout Container
        self.add(patGrid)
        patGrid.props.valign = Gtk.Align.CENTER
        patGrid.props.halign = Gtk.Align.CENTER

        self.firstNameLabel = Gtk.Label("First Name: ")
        self.firstNameEntry = Gtk.Entry()

        patGrid.attach(self.firstNameLabel, 1, 1, 2, 2)
        patGrid.attach_next_to(self.firstNameEntry, self.firstNameLabel, 1, 2, 2) #left=0, r=1, t=2, b=3

        self.lastNameLabel = Gtk.Label("Last Name: ")
        self.lastNameEntry = Gtk.Entry()

        patGrid.attach_next_to(self.lastNameLabel,self.firstNameLabel, 3, 2, 2)
        patGrid.attach_next_to(self.lastNameEntry, self.lastNameLabel, 1, 2, 2)


        self.submitButton = Gtk.Button(label="Submit")
        self.submitButton.connect("clicked", self.on_submitButton_clicked)
        patGrid.attach_next_to(self.submitButton, self.lastNameLabel, 3, 4, 2)

    def on_submitButton_clicked(self, widget):
        firstNameVar = self.firstNameEntry.get_text()
        lastNameVar = self.lastNameEntry.get_text()

        if firstNameVar != "" and lastNameVar != "":
            time = datetime.now()
            timeStr = time.strftime("%H-%M-%b%d-%Y") # Hour-Minute-MonthDay-Year

            print(firstNameVar + ' ' + lastNameVar)
            currentPatientFileName = lastNameVar + "_" + firstNameVar + "_" + timeStr
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

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("pelvisim.png",100,100,True)
        pelvIm = Gtk.Image.new_from_pixbuf(pixbuf)
        initGrid.add(pelvIm)

    def on_beginButton_clicked(self, widget):
        print("Begin Button Clicked")



win = Application()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
