from engine import *
from gamelogic import *
from cards import *

class CardSprite(Sign):
    def __init__(self, card, position=Vector2(0, 0)):
        super().__init__(background=card.type.portrait,
                         text='Stats here',
                         position=position,
                         text_shift=Vector2(50, 120),
                         font_size=22)
        self.dragging = False

    def tick(self, dt):
        super().tick(dt)
        if pyglet.window.mouse_impulse:
            if self.dragging:
                self.dragging = False
            elif self.pointIntersection(pyglet.window.mouse_position):
                self.dragging = True
        
        if self.dragging:
            dist = pyglet.window.mouse_position - self.center
            self.move(*(dist / 10))

class Board:
    def __init__(self):
        self.player_1 = RandyAI()
        self.player_2 = RandyAI()

    def random_deck(self, stock=None):
        if stock:
            return random.shuffle(stock)
        ...