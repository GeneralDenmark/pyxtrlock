import pyglet
import pyscreenshot
import os
import threading
from PIL import ImageFilter


class Window(pyglet.window.Window):
    def __init__(self, _screen, img_name):
        super(Window, self).__init__(_screen.width, _screen.height)
        self.__screen = _screen
        self.img_name = img_name
        self.background = pyglet.resource.image(img_name)

        #sprites= [
        #    pyglet.sprite.Sprite()
        #]
        self.batches = {}

        self.alive = 1
        self.render()

    def on_draw(self):
        self.render()

    def render(self):
        self.set_location(self.__screen.x, 0)
        self.clear()
        self.background.anchor_x = self.background.width
        self.background.anchor_y = self.background.height
        self.background.blit(self.width ,  self.height)
        for batch_name, batch in self.batches.items():
            batch.draw()
        self.flip()


def create_screen():
    resources = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'resources')
    pyglet.resource.path = [resources]
    pyglet.resource.reindex()

    display = pyglet.canvas.get_display()
    screens = display.get_screens()
    count = 0
    windows = []
    for screen in sorted(screens, key=lambda e: e.x):
        im = pyscreenshot.grab((
            screen.x, 0, screen.x + screen.width, screen.height
        ))
        im = im.filter(ImageFilter.GaussianBlur(radius=5))
        im.save(os.path.join(resources, str(count) + '.png'))
        count += 1

    count = 0
    for screen in sorted(screens, key=lambda e: e.x):
        window = Window(screen, str(count) + '.png')
        windows.append(window)
        count += 1

    threading.Thread(target=run).start()


def run():
    pyglet.app.run()


def kill_screen():
    pyglet.app.exit()


if __name__ == '__main__':
    create_screen()
