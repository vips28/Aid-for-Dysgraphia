# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:29:53 2021

@author: myanacondadont
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class MyGrid(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == '__main__':
    MyApp().run()