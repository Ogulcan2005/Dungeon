import random
import time

def kamer_3(player_defense, player_attack):
    items = ['schild', 'zwaard']
    item = random.choice(items)
    
    if item == 'schild':
        player_defense += 1
    else:
        player_attack += 2
    
    print('Je duwt hem open en stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item}.')
    print(f'Je pakt het {item} op en houdt het bij je.')
    
    if item == 'schild':
        print(f'Het {item} geeft je meer defense. Je defense is nu {player_defense}.')
    else:
        print(f'Het {item} geeft je meer attack. Je attack is nu {player_attack}.')
    
    print('Op naar de volgende deur.')
    print("")
    time.sleep(1)
    
    return player_defense, player_attack, item

import math

def kamer_6(player_defense, player_attack, player_health):
    print("Kamer 6\n")
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    
    print('Dapper zonder loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        
        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health - zombie_attack_amount}.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()



