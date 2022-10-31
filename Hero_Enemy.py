from asyncio import start_server
from decimal import ConversionSyntax
from email.headerregistry import ContentDispositionHeader
from opcode import stack_effect
from sys import builtin_module_names
from xmlrpc.client import Boolean


Hero = {
    'name': 'Teenage Mutant Ninja Turtles',
    'level': 1,
    'health': 100,
    'equipment': 'Nunchucks, Sai, Katana, Bo Staff',
    'attacks': 'power kicks, power punches, Equipment',

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
    'attacks': 'kicks, punches, Equipment',

    'Coins': {
        'Copper': 300,
        'Silver': 200,
        'Gold': 100,
            }
}
]
    

Enemy_two = [
{
    'Name': 'Rocksteady',
    'Level': 2,
    'Health': 100,
    'Equipment': 'Kama, Eku, Tekko, Nunti Bo',
    'attacks': 'kicks, punches, Equipment',

    'Coins': {
        'Copper': 300,
        'Silver': 200,
        'Gold': 100,
            }
}            
]
    

Enemy_three = [
{
    'Name': 'Foot Clan',
    'Level': 3,
    'Equipment': 'Ninja Stars, Katana, Smoke Grenades',
    'attacks': 'kicks, punches, Equipment',

    'Coins': {
        'Copper': 300,
        'Silver': 200,
        'Gold': 100,
            }
}
]    

print(Hero['name'])