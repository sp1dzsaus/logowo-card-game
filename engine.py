from mymaths import Vector2
import pyglet

class Sprite:
    def __init__(self, image: pyglet.image.ImageData, position=Vector2(0, 0)):
        self.image = image
        self.pos = position

    def move(self, x, y):
        self.pos += Vector2(x, y)

    def render(self):
        self.image.blit(*self.pos.tuple())

    @property
    def center(self):
        return self.pos + Vector2(self.image.width,
                                  self.image.height) / 2

    def tick(self, dt):
        pass

class Sign(Sprite):
    def __init__(self, background, text, position=Vector2(0, 0),
                 text_shift=Vector2(0, 0),
                 **kwargs):
        super().__init__(image=background, position=position)
        self.label = pyglet.text.Label(text,
                                       x=position.x + text_shift.x,
                                       y=position.y + text_shift.y,
                                       **kwargs)
        self.text_shift = text_shift

    def syncLabelPosition(self):
        self.label.position = (self.pos + self.text_shift).tuple()

    def setText(self, text):
        self.label.text = text
        
    def render(self):
        super().render()
        self.syncLabelPosition()
        self.label.draw()
        

class CardSprite(Sign):
    def __init__(self, card, position=Vector2(0, 0)):
        super().__init__(background=card.type.portrait,
                         text='Stats here',
                         position=position,
                         text_shift=Vector2(50, 120),
                         font_size=22)

    def tick(self, dt):
        dist = pyglet.window.mouse_position - self.center
        self.move(*(dist / 10))
        