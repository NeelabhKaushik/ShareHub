from kivy.lang import Builder
from kivymd.app import MDApp
from plyer import filechooser
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
import os
import os.path
from kivymd.toast import toast
import socket
import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import png
import os
import getpass
import time
import socket
import select
from threading import *
import sys


class MainApp(MDApp):
    
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        self.title='KivyMD Dashboard'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("share.kv"))
        screen_manager.add_widget(Builder.load_file("send.kv"))
        return screen_manager
        
    def file_chooser(self):
        filechooser.open_file(on_selection = self.selected)
            
    def selected(self, selection):
        global filename
        filename = os.path.basename(selection[0])
        global file_loc
        file_loc = selection[0]
    def send(self):
        import getpass
        envr = getpass.getuser()

        PORT = 8090
        # this finds the name of the computer user
        
        
        # changing the directory to access the files desktop
        # with the help of os module
        fileloc = os.path.dirname(file_loc)
        desktop = fileloc
        os.chdir(desktop)
        
        
        Handler = http.server.SimpleHTTPRequestHandler
        hostname = socket.gethostname()
        
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
        link = IP
        
        url = pyqrcode.create(link)
        screen_manager.get_screen("share").ids.pdf.text = str(url)
        url.png('myqr.png', scale = 6)
        webbrowser.open('myqr.png')
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            print("Type this in your Browser", IP)
            print("or Use the QRCode")
            httpd.serve_forever()
MainApp().run()