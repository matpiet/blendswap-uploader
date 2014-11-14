#!/usr/bin/env python

"""
HTTP Client for API tests,
Don't put too much work in here!
Use it just to test concepts!
"""

import pygtk
pygtk.require("2.0")
import gtk, sys, json
import httplib2


# Create app and render it
# check for cookie presence
# if no cookie
# 	ask for cedentials
# else
# 	validate cookie against server
# 	if cookie is invalid
# 		ask for credentials
#
# continue to normal UI

host = "http://blendswap.dev"

whoamiURL = host + "/users/whoami.json"

loginURL = host + "/users/login.json"


class Client():

	http = httplib2.Http(".cache")

	def __init__(self):
		self.setup_main_window()
		self.setup_ui_elements()
		self.window.show_all()
		self.check_login()

	def setup_main_window(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_icon_from_file("icon.png")
		self.window.set_title("HTTP Client 0.0")
		self.window.set_size_request(300,400)
		self.window.connect("destroy", gtk.main_quit)

	def setup_ui_elements(self):
		self.rootBox = gtk.VBox(spacing=8)
		self.label = gtk.Label("Looking you up")
		self.button = gtk.Button("Check status")
		self.button.connect("clicked", self.check_login)
		# Add ui elements to box and window
		self.rootBox.pack_start(self.label)
		self.rootBox.pack_start(self.button)
		self.window.add(self.rootBox)

	def change_notice(self, newText):
		self.label.set_text(newText)
		return

	def check_login(self, widget=None):
		print "Login check"


if (__name__ == "__main__"):
	client = Client()
	gtk.main()

