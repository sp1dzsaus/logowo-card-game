import pyglet
from pyglet.window import key
from pyglet.gl import *

from gamelogic import *

window = pyglet.window.Window(1280, 600)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

window.set_caption('Logowo: The Card Game')

@window.event
def on_draw():
    window.clear()
    for shift, testcard in enumerate(testcards):
        testcard.getImage().blit(shift * 300, 0)

@window.event
def on_key_press(symbol, modifiers):
    pass
        
@window.event
def on_mouse_press(x, y, button, modifiers):
    pass

def tick(dt):
    FPS = pyglet.clock.get_fps()

testcards = []
def test():
    card1 = SuperheavySimon()
    card1.spell_genocide()
    testcards.append(card1)
    card2 = TheBook()
    testcards.append(card2)


if __name__ == '__main__':
    test()
    pyglet.clock.schedule_interval(tick, 1)

    pyglet.app.run()
