########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# App class: App initializer                                           #
#                                                                      #
# Created on 2016-12-29                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants import *   # Constants file

########################################################################
#                                                                      #
#                               APP CLASS                              #
#                                                                      #
########################################################################

class App(object):
    def __init__(self, appDirectory):
        self.appDirectory = appDirectory

        print MESSAGE
