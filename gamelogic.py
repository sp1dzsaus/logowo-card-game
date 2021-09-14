from pyglet.image import load as pygletimage
from pyglet.gl import *
from pyglet.text import Label
from random import randint, choice


def image(filename):
    return pygletimage(f'assets/textures/{filename}.png')

class CardType:
    # Default parameters
    max_hp = 10
    portrait = image('cards/what')
    spells = {}
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __call__(self, *args, **kwargs):
        return Card(self, *args, **kwargs)

    def spell(self, name):
        def wrapped(func):
            self.spells[name] = func
            return func
        return wrapped

SuperheavySimon = CardType(portrait=image('cards/superheavy-simon'))
@SuperheavySimon.spell('genocide')
def genocide(*args):
    print('Test spell')

TheBook = CardType()

class Card:
    def __init__(self, type: CardType):
        self.type = type
        self.hp = type.max_hp

    def getImage(self):
        base = self.type.portrait.get_texture()
        label = Label('Hello, world',
                      font_name='Times New Roman',
                      font_size=36,
                      x=50, y=150,
                      anchor_x='center', anchor_y='center')
        glBindTexture(GL_TEXTURE_2D, base.id)
        label.draw()
        return base
        

    def __getattr__(self, name):
        spell_prefix = 'spell_'
        if name.startswith(spell_prefix):
            return self.type.spells[name[len(spell_prefix):].lower()]
        raise AttributeError(f"type object 'Card' has no attribute '{name}'")
   
