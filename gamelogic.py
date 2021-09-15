from pyglet.image import load as pygletimage

def image(filename):
    return pygletimage(f'assets/textures/{filename}.png')


class Spell:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __call__(self, *args):
        return self.func(*args)


class CardType:
    # Default parameters
    max_hp = 10
    portrait = image('cards/what')
    spells = {}

    def __init__(self, portrait, **kwargs):
        self.portrait = image(portrait)
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __call__(self, *args, **kwargs):
        return Card(self, *args, **kwargs)

    def spell(self, name, icon):
        def wrapped(func):
            self.spells[name] = Spell(func=func,
                                      icon=icon)
            return func
        return wrapped


class Card:
    def __init__(self, type: CardType):
        self.type = type
        self.hp = type.max_hp

    def __getattr__(self, name):
        spell_prefix = 'spell_'
        if name.startswith(spell_prefix):
            return self.type.spells[name[len(spell_prefix):].lower()]
        raise AttributeError(f"type object 'Card' has no attribute '{name}'")
      