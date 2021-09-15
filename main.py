import pyglet
from pyglet.window import key
from pyglet.gl import *

from engine import *
from cards import *

window = pyglet.window.Window(1280, 1200)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

window.set_caption('Logowo: The Card Game')
pyglet.window.mouse_position = Vector2(0, 0)

@window.event
def on_draw():
    window.clear()
    for sprite in sprites:
        sprite.render()

@window.event
def on_mouse_motion(x, y, dx, dy):
    pyglet.window.mouse_position = Vector2(x, y)

@window.event
def on_key_press(symbol, modifiers):
    pass
        
@window.event
def on_mouse_press(x, y, button, modifiers):
    pass

def tick(dt):
    FPS = pyglet.clock.get_fps()
    for sprite in sprites:
        sprite.tick(dt)

sprites = []
def test():
    card1 = SuperheavySimon()

    sprite = CardSprite(card1,
                        Vector2(10, 10))
    sprites.append(sprite)


if __name__ == '__main__':
    test()
    pyglet.clock.schedule_interval(tick, 0.002)
    pyglet.app.run()
