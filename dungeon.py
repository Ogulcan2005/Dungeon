import random
import time
import math
from functions import *

player_attack = 1
player_defense = 0
player_health = 3
ruppee = 0


# === [kamer 1] === #
print("Kamer 1\n")
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

ruppee = kamer_7(ruppee)

print("je kunt nu 2 richtingen kiezen")
print("je kunt door gaan via kamer 2 of gelijk gaan naar kamer 8")
kamer2_8 = input("welke kamer wil je naar toe gaan")
if kamer2_8 == "8":
    ruppee, player_health = kamer_8(ruppee, player_health)
    print('Je kan nu kiezen om naar kamer 9 tegaan of naar kamer 3.')
    kiez_kamer1 = input('Kies naar welke kamer je wilt gaan (9 of 3): ')
    if kiez_kamer1 == "9":
        player_defense, player_health = kamer_9(player_defense, player_health)
        item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)
    else:
        item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)
elif kamer2_8 == "2":
    ruppee = kamer_2(ruppee)
    print('Je kan nu kiezen om naar kamer 3 tegaan of naar kamer 6 via kamer 6 kom je weer uit op kamer 3.')
    kamer = input('Kies naar welke kamer je wilt gaan (6 of 8): ')
    if kamer == "6":
        kamer_6(player_defense, player_attack, player_health)
        print('Je kan nu kiezen om naar kamer 3 tegaan of naar kamer 8.')
        kiez_kamer = input('Kies naar welke kamer je wilt gaan (8 of 3): ')
        if kiez_kamer == "8":
            ruppee, player_health = kamer_8(ruppee, player_health)
            print('Je kan nu kiezen om naar kamer 9 tegaan of naar kamer 3.')
            kiez_kamer2 = input('Kies naar welke kamer je wilt gaan (9 of 3): ')
            if kiez_kamer2 == "9":
                player_defense, player_health = kamer_9(player_defense, player_health)
                item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)
            else:
                item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)
        else:
            item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)
    else:
        ruppee, player_health = kamer_8(ruppee, player_health)
        kiez_kamer3 = input('Kies naar welke kamer je wilt gaan (9 of 3): ')
        if kiez_kamer3 == "9":
            player_defense, player_health = kamer_9(player_defense, player_health)
            item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)
        else:
            item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)
kamer_4(player_defense, player_attack, player_health)
kamer_10(player_defense, player_attack, player_health)
kamer_5()





