import subprocess
import pyglet
import pyscreenshot
import os
from PIL import ImageFilter
from time import sleep

DIR = os.path.abspath(os.path.dirname(__file__))

locked_bg = os.path.join(DIR, 'output.png')
platform = pyglet.window.get_platform()
display = pyglet.canvas.get_display()
screens = display.get_screens()

width = 0
im = pyscreenshot.grab((
    width, 0, width + screens[0].width, 1200
))
width += screens[0].width
im = im.filter(ImageFilter.GaussianBlur(radius=5))
im.save(os.path.join(DIR, '0') + '.png')
width += screens[0].width
im = pyscreenshot.grab((
    width, 0, width + screens[2].width, 1200
))
width += screens[2].width
im = im.filter(ImageFilter.GaussianBlur(radius=5))
im.save(os.path.join(DIR, '1') + '.png')
im = pyscreenshot.grab((
    width, 0, width + screens[1].width, 1200
))
im = im.filter(ImageFilter.GaussianBlur(radius=5))
im.save(os.path.join(DIR, '2') + '.png')


width = 0
window1 = pyglet.window.Window(screens[0].width, screens[0].height)
window1.set_location(width, 0)
width += screens[0].width
window2 = pyglet.window.Window(screens[2].width, screens[2].height)
window2.set_location(width, 0)
width += screens[2].width
window3 = pyglet.window.Window(screens[1].width, screens[1].height)
window3.set_location(width, 0)
img1 = pyglet.resource.image('0.png')
img2 = pyglet.resource.image('1.png')
img3 = pyglet.resource.image('2.png')


@window1.event
def on_draw():
    window1.clear()
    print(window1.height, 'x', window1.width)

    print(img1.width, ' x ', img1.height)
    img1.anchor_x = img1.width // 2
    img1.anchor_y = img1.height // 2
    img1.blit(window1.width // 2, (window1.height - 120) // 2)


@window2.event
def on_draw():
    print(window2.height, 'x', window2.width)

    window2.clear()
    print (img2.width, ' x ', img2.height)
    img2.anchor_x = img2.width // 2
    img2.anchor_y = img2.height // 2
    img2.blit(window2.width // 2, window2.height // 2)


@window3.event
def on_draw():
    print(window3.height, 'x', window3.width)
    window3.clear()
    print (img3.width, ' x ', img3.height)
    img3.anchor_x = img3.width // 2
    img3.anchor_y = img3.height // 2
    img3.blit(window3.width // 2, window3.height // 2)


pyglet.app.run()
