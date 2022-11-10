# when BePop wins, it does not go back to the beginning
# the math is not adding up right...

from Hero_Enemy import Hero, Enemy_one, Enemy_two, Enemy_three
import random


while Hero['health'] > 0 and Enemy_one['Health'] > 0:

    random_attacks = random.choice(Hero['attacks'])
    print(Hero['name'], "strike with", random_attacks[0])  
    Enemy_one['Health'] -= random_attacks[1]
    print(Enemy_one['Name'], "has",Enemy_one['Health'], "health left.")

    print(" ")

    random_attacks2 = random.choice(Enemy_one['attacks'])
    print(Enemy_one['Name'], "strikes with", random_attacks2[0])
    Hero['health'] -= random_attacks2[1]
    print(Hero['name'], "has",Hero['health'], "health left.")    

    print(" ")

    if Enemy_one['Health'] > 0:

        print(Enemy_one['Name'], "strikes with", random_attacks2[0])
    Hero['health'] -= random_attacks2[1]
    print(Hero['name'], "has",Hero['health'], "health left.")

    if Hero['health'] > 0:

        print(Hero['name'], "strikes with", random_attacks[0])
    Enemy_one['Health'] -= random_attacks[1]
    print(Enemy_one['Name'], "has",Enemy_one['Health'], "health left.")
         
    if Hero['health'] > Enemy_one['Health']:
        print(f"{Hero['name']} defeated {Enemy_one['Name']}. You are moving up to Level 2.")
        print(f"{Hero['name']} now has {Hero['equipment']}, {Enemy_one['Equipment']}")
        break
    else:
        print(f"{Enemy_one['Name']} defeated {Hero['name']}. Try again.") 
        False    

while Hero['health2'] > 0 and Enemy_two['Health'] > 0:

    random_attacks = random.choice(Hero['attacks'])
    print(Hero['name'], "strike with", random_attacks[0])  
    Enemy_two['Health'] -= random_attacks[1]
    print(Enemy_two['Name'], "has",Enemy_two['Health'], "health left.")

    print(" ")

    random_attacks3 = random.choice(Enemy_two['attacks'])
    print(Enemy_two['Name'], "strikes with", random_attacks3[0])
    Hero['health2'] -= random_attacks3[1]
    print(Hero['name'], "has",Hero['health2'], "health left.")    

    print(" ")

    if Enemy_two['Health'] > 0:
        print(Enemy_two['Name'], "strikes with", random_attacks3[0])
    Hero['health'] -= random_attacks3[1]
    print(Hero['name'], "has",Hero['health'], "health left.")

    if Hero['health'] > 0:

        print(Hero['name'], "strikes with", random_attacks[0])
    Enemy_two['Health'] -= random_attacks[1]
    print(Enemy_two['Name'], "has",Enemy_two['Health'], "health left.")
         
    if Hero['health2'] > Enemy_one['Health']:
        print(f"{Hero['name']} defeated {Enemy_two['Name']}. You are moving up to Level 3.")
        print(f"{Hero['name']} now has {Hero['equipment']}, {Enemy_one['Equipment']}, {Enemy_two['Equipment']}")
        break
    else:
        print(f"{Enemy_two['Name']} defeated {Hero['name']}. Try again.")
        False

while Hero['health3'] > 0 and Enemy_three['Health'] > 0:

    random_attacks = random.choice(Hero['attacks'])
    print(Hero['name'], "strike with", random_attacks[0])  
    Enemy_three['Health'] -= random_attacks[1]
    print(Enemy_three['Name'], "has",Enemy_three['Health'], "health left.")

    print(" ")

    random_attacks4 = random.choice(Enemy_three['attacks'])
    print(Enemy_three['Name'], "strikes with", random_attacks4[0])
    Hero['health3'] -= random_attacks4[1]
    print(Hero['name'], "has",Hero['health3'], "health left.")    

    print(" ")

    if Enemy_three['Health'] > 0:

        print(Enemy_three['Name'], "strikes with", random_attacks3[0])
    Hero['health'] -= random_attacks3[1]
    print(Hero['name'], "has",Hero['health'], "health left.")

    if Hero['health'] > 0:

        print(Hero['name'], "strikes with", random_attacks[0])
    Enemy_three['Health'] -= random_attacks[1]
    print(Enemy_three['Name'], "has",Enemy_three['Health'], "health left.")
         
    if Hero['health3'] > Enemy_one['Health']:
        print(f"{Hero['name']} defeated {Enemy_three['Name']}. You win.")
        print(f"{Hero['name']} now has {Hero['equipment']}, {Enemy_one['Equipment']}, {Enemy_two['Equipment']}, {Enemy_three['Equipment']}")
        break
    else:
        print(f"{Enemy_three['Name']} defeated {Hero['name']}. Try again.")
        False