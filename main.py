import pyglet
from pyglet.window import key
from pyglet.gl import *

from engine import *
from cards import *
from gamelogic import *

window = pyglet.window.Window(1280, 1200)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

window.set_caption('Logowo: The Card Game')
pyglet.window.mouse_position = Vector2(0, 0)
pyglet.window.mouse_pressed = False
pyglet.window.mouse_impulse = None

@window.event
def on_draw():
    window.clear()

@window.event
def on_mouse_motion(x, y, dx, dy):
    pyglet.window.mouse_position = Vector2(x, y)

@window.event
def on_key_press(symbol, modifiers):
    pass
        
@window.event
def on_mouse_press(x, y, button, modifiers):
    pyglet.window.mouse_pressed = True
    if pyglet.window.mouse_impulse is None:
        pyglet.window.mouse_impulse = True
    
@window.event
def on_mouse_release(x, y, button, modifiers):
    pyglet.window.mouse_pressed = False
    pyglet.window.mouse_impulse = None
    


def tick(dt):
    FPS = pyglet.clock.get_fps()
    print('Player 1:')
    print(*players[0].active_cards, sep=' || ')
    print('deck:[', end='')
    print(*players[0].deck, sep=', ', end='')
    print(']', end='\n\n')

    print('Player 2:')
    print(*players[1].active_cards, sep=' || ')
    print('deck:[', end='')
    print(*players[1].deck, sep=', ', end='')
    print(']', end='\n\n')

    print('Player 1 turn')
    players[0].turn(players[1])
    print('Player 2 turn')
    players[1].turn(players[0])
    print('\n===============\n')

    if pyglet.window.mouse_impulse:
        pyglet.window.mouse_impulse = False

players = []
def test():
    r1 = RandyAI([SuperheavySimon(), Superman(),
                  Sosiska(), Forgor(), TheBook()])
    r2 = RandyAI([SuperheavySimon(), Superman(),
                  Sosiska(), Forgor(), TheBook()])
    players.append(r1)
    players.append(r2)
    r1.turn(r2, first_turn=True)
    r2.turn(r1, first_turn=True)


if __name__ == '__main__':
    test()
    pyglet.clock.schedule_interval(tick, 1)
    pyglet.app.run()
