from pyglet.image import load as pygletimage
import random

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
                                      icon=icon,
                                      name=name)
            return func
        return wrapped

    def __str__(self):
        return self.name


class Card:
    def __init__(self, type: CardType):
        self.type = type
        self.hp = type.max_hp

    def cast_spell(self, name, *args):
        return self.type.spells[name](*args)
    
    def __getattr__(self, name):
        spell_prefix = 'spell_'
        if name.startswith(spell_prefix):
            return self.type.spells[name[len(spell_prefix):].lower()]
        raise AttributeError(f"type object 'Card' has no attribute '{name}'")

    def __str__(self):
        return str(self.type)


class AbstractPlayer:
    def __init__(self, deck: list):
        for card in deck:
            card.owner = self
        self.deck = deck
        self.active_cards = [None, None, None]

    def turn(self, opponent, first_turn=False):
        pass

    def changeActiveCard(self, i, card: Card):
        self.deck.remove(card)
        if self.active_cards[i]:
            self.deck.append(self.active_cards[i])
        self.active_cards[i] = card

    def castCardSpell(self, attacker: Card, spellname, target: Card):
        attacker.cast_spell(spellname, target)


class RandyAI(AbstractPlayer):
    def turn(self, opponent, first_turn=False):
        decklen = len(self.deck)
        if first_turn:
            for i in range(3):
                self.changeActiveCard(i, random.choice(self.deck))
            return

        if random.randint(1, 4) == 1:
            self.changeActiveCard(random.randint(1, 3), random.choice(self.deck))
        else:
            target = random.choice([card for card in opponent.active_cards if card])
            attacker = random.choice([card for card in self.active_cards if card])
            spellname = random.choice(list(attacker.type.spells.keys()))
            self.castCardSpell(attacker, spellname, target)