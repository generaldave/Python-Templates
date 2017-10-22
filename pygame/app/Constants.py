'''
David Fuller

Constants file - File contains application constants.

10-15-2017
'''

__all__ = ['background_color', 'screen_resolution', 'app_title', 'fps']

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
color = namedtuple('color', ['r', 'g', 'b'])
resolution = namedtuple('resolution', ['width', 'height'])

background_color = color(r = 127, g = 127, b = 127)
screen_resolution = resolution(width = 840, height = 480)

app_title = "Pygame Template"
fps = 60
