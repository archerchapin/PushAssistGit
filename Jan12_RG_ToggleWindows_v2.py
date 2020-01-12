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

    def homeWindow(self,widget):
        """
        """
        #self.mainGrid = Gtk.Grid()
        #self.add(self.mainGrid)
        self.mainBox = Gtk.VBox()
        self.add(self.mainBox)

        self.labelGrid = Gtk.Grid()
        self.homePageLabel = Gtk.Label("PUSH ASSIST HOME PAGE")

        self.labelGrid.attach(self.homePageLabel,1,1,2,2)
        self.mainBox.add(self.labelGrid)

        self.labelGrid.props.valign = Gtk.Align.CENTER
        self.labelGrid.props.halign = Gtk.Align.CENTER

        # ADDING AND REMOVING SUB GRID WORKS:
        #self.mainBox.remove(self.labelGrid)
        #self.mainBox.add(self.labelGrid)

        self.homeButtonGrid = Gtk.Grid()
        self.mainBox.add(self.homeButtonGrid)

        self.homeButtonGrid.props.halign = Gtk.Align.CENTER
        self.homeButtonGrid.props.valign = Gtk.Align.END

        self.openButton = Gtk.Button("Open...")
        self.openButton.connect("clicked", self.on_openButton_clicked)
        self.homeButtonGrid.attach(self.openButton,1,1,2,2)

        self.newPatButton = Gtk.Button("New Patient")
        self.newPatButton.connect("clicked", self.on_newPatButton_clicked)
        self.homeButtonGrid.attach_next_to(self.newPatButton, self.openButton,1,2,2) #left=0, r=1, t=2, b=3

        self.backButton = Gtk.Button("Back")
        self.backButton.connect("clicked", self.on_backButton_clicked)
        self.homeButtonGrid.attach_next_to(self.backButton, self.newPatButton,1,1,1)

    def newPatWindow(self, widget):
        """
        """
        print("New Pat Window")
        self.mainBox.remove(self.labelGrid)

        #self.mainBox.add(self.testButton)
        #self.patGrid = Gtk.Grid()
        #self.mainBox.remove(self.labelGrid)
        #self.mainBox.add(self.patGrid)

        #self.firstNameLabel = Gtk.Label("First Name: ")
        #self.firstNameEntry = Gtk.Entry()

        #self.patGrid.attach(self.firstNameLabel, 1, 1, 2, 2)
        #self.patGrid.attach_next_to(self.firstNameEntry, self.firstNameLabel, 1, 2, 2) #left=0, r=1, t=2, b=3

    def on_openButton_clicked(self, widget):
        """
        TODO: Actually have a file selecting window pop up here
        """
        print("Open... Button")

    def on_newPatButton_clicked(self, widget):
        """
        """
        print("New Patient Button")
        self.newPatWindow(Gtk.Window)

    def on_backButton_clicked(self, widget):
        """
        """
        print("Back Button")
        #self.homeWindow(Gtk.Window)

run = Application()
run.connect("destroy", Gtk.main_quit)
run.show_all()
Gtk.main()
