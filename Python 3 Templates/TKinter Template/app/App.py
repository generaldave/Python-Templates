################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# App class: App initializer                                                   #
#                                                                              #
# Created on 2017-9-2                                                          #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from .Constants import *   # Constants file
from tkinter    import *   # For GUI

################################################################################
#                                                                              #
#                                   APP CLASS                                  #
#                                                                              #
################################################################################

class App(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, appDirectory: str) -> None:
        self.appDirectory = appDirectory

        # Set up GUI
        self.root = None
        self.setupGUI()

        # Run app
        self.runApp()

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Mehtod sets up GUI
    def setupGUI(self) -> None:
        # Screen attributes
        self.root = Tk()
        self.root.title(APP_TITLE)
        self.root.geometry(SCREEN_RESOLUTION)

    # Method runs app
    def runApp(self) -> None:
        self.root.mainloop()
