# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:30:42 2021

@author: myanacondadont
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class MyGrid(Widget):
    pass

class HomeApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == '__main__':
    HomeApp().run()