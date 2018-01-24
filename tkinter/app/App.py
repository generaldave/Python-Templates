'''
David Fuller

App class: Initializes application

10-22-2017
'''

import sys

from .Constants import *

if sys.version_info >= (3, 0):
    from tkinter import *
else:
    from Tkinter import *

class App(object):
    '''
    Sets up and runs a Pygame application.
    '''
    
    def __init__(self, app_directory):
        '''
        App's init method.

        Stores application directory. Runs the applicaiton.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.app_directory = app_directory

        self.root = None
        self.setup_GUI()

        self.run_app()

    def setup_GUI(self):
        '''
        Method sets up the graphical user interface.

        Initializes Tkinter. Sets up the window size and title.
        '''
        
        self.root = Tk()
        self.root.title(app_title)
        self.root.geometry(screen_resolution)

    def run_app(self):
        '''
        Runs Tkinter application.
        '''
        
        self.root.mainloop()
