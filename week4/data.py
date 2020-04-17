import os
'''
I need to check out the convention for this.
Can I use JSON instead?
'''

dk_data = os.path.dirname(
    os.path.realpath(__file__)) + "/resources/befkbhalderstatkode.csv"


neighb = {
    1: 'Indre By',
    2: 'Østerbro',
    3: 'Nørrebro',
    4: 'Vesterbro/Kgs. Enghave',
    5: 'Valby',
    6: 'Vanløse',
    7: 'Brønshøj-Husum',
    8: 'Bispebjerg',
    9: 'Amager Øst',
    10: 'Amager Vest',
    99: 'Udenfor'
}