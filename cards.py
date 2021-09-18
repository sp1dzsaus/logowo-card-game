from gamelogic import CardType

SuperheavySimon = CardType(portrait='cards/superheavy-simon', name='SuperheavySimon')
@SuperheavySimon.spell('genocide', None)
def genocide(*args):
    print('Simon - Genocide!!!')

@SuperheavySimon.spell('bubik', None)
def bubik(*args):
    print('Bubik Kubik')


TheBook = CardType(portrait='cards/what', name='TheBook')
@TheBook.spell('dms', None)
def dms(*args):
    print('Read DMS you dumbhead')
    
@TheBook.spell('bob', None)
def bob(*args):
    print('TONNIE BEST')


Sosiska = CardType(portrait='cards/sosiska', name='God Tier Food')
@Sosiska.spell('lmao', None)
def lmao(*args):
    print('The food of the legends')
    
@Sosiska.spell('myka', None)
def myka(*args):
    print('Remember when shcito was')
    

Forgor = CardType(portrait='cards/senior', name='Trollge Dementia')
@Forgor.spell('daughter', None)
def daughter(*args):
    print('What was my daughters name?')
    
@Forgor.spell('remember', None)
def remember(*args):
    print('actually no I do not remember')


Superman = CardType(portrait='cards/legend', name='Legend')
@Superman.spell('twenty_six', None)
def twenty_six(*args):
    print('epic number 25')
    
@Superman.spell('purp', None)
def purp(*args):
    print('epic color green')
