#from asyncio import start_server
#from decimal import ConversionSyntax
#from email.headerregistry import ContentDispositionHeader
#from opcode import stack_effect
#from sys import builtin_module_names
#from xmlrpc.client import Boolean



Hero = {
    'name': 'Teenage Mutant Ninja Turtles',
    'level': 1,
    'health': 100,
    'equipment': 'Nunchucks, Sai, Katana, Bo Staff',
    'attacks': [
        (('power kicks, 200), (power punches, 100), ([equipment], 500)')),

    'Coins': {
        'Copper': 300,
        'Silver': 200,
        'Gold': 100,
            }
}       

Enemy_one = [
{
    'Name': 'Bebop',
    'Level': 1,
    'Health': 100,
    'Equipment': 'Hanbo, Tonfa, Tanbo, Sansetsuko',
    'attacks': (('kicks, 20'), ('punches, 10'), ('Hanbo', 50'), ('Tonfa, 50'),
                ('Tanbo, 50'), ('Sanetsuko, 50'))),

    'Coins': {
        'Copper': 300,
        'Silver': 200,
        'Gold': 100
            }
}
]

Enemy_two = [
{
    'Name': 'Rocksteady',
    'Level': 2,
    'Health': 100,
    'Equipment': 'Kama, Eku, Tekko, Nunti Bo',
    'attacks': (('kicks, 20') ('punches, 10'), ('Kama, 50'),
                ('Eku, 50'), ('Tekko, 50'), ('Nunti Bo, 50'))),

    'Coins': {
        'Copper': 300,
        'Silver': 200,
        'Gold': 100
            }
}
]

Enemy_three = [
{
    'Name': 'Foot Clan',
    'Level': 3,
    'Equipment': 'Ninja Stars, Katana, Smoke Grenades',
    'attacks': (('kicks, 20'), ('punches, 10'), ('Ninja Stars, 50'), 
                ('Katana, 50'), ('Smoke Grenades, 50'))),

    'Coins': {
        'Copper': 300,
        'Silver': 200,
        'Gold': 100,
            } 
}
]

enemy_list = {
    "Enemy_one" : Enemy_one,
    "Enemy_two" : Enemy_two,
    "Enemy_three" : Enemy_three
}


import random
enemy_attacks = "enemy_one[attacks]", "enemy_two[attacks]", "enemy_three[attacks]"

rand_int = random.randrange(0-5)
print(enemy_one[attacks]})


