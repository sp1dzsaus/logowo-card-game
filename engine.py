from mymaths import Vector2
import pyglet

class Sprite:
    def __init__(self, image: pyglet.image.ImageData, position=Vector2(0, 0), hitbox=None):
        self.image = image
        self.pos = position
        if not hitbox:
            self.hitbox = Vector2(image.width, image.height)
        else:
            self.hitbox = hitbox

    def move(self, x, y):
        self.pos += Vector2(x, y)

    def render(self):
        self.image.blit(*self.pos.tuple())

    @property
    def center(self):
        return self.pos + self.hitbox / 2

    def setImage(self, image):
        if self.hitbox == Vector2(self.image.width, self.image.height):
            self.hitbox = Vector2(image.width, image.height)
        self.image = image

    def pointIntersection(self, point_pos):
        a = self.pos
        b = self.pos + self.hitbox
        return a.x < point_pos.x < b.x and a.y < point_pos.y < b.y
    
    def tick(self, dt):
        pass

class Sign(Sprite):
    def __init__(self, background, text, position=Vector2(0, 0),
                 text_shift=Vector2(0, 0), hitbox=None,
                 **kwargs):
        super().__init__(image=background, position=position, hitbox=hitbox)
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

        