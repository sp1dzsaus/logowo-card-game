from gamelogic import CardType

SuperheavySimon = CardType(portrait='cards/superheavy-simon')
@SuperheavySimon.spell('genocide', None)
def genocide(*args):
    print('Test spell')

TheBook = CardType(portrait='cards/what')
