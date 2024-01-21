import random
import time
import math

def kamer_3(player_defense, player_attack, ruppees):
    print("Kamer 3\n")
    print(f'Je loopt nu binnen de volgende kamer en vind daar binnen een goblin merchant')
    print(f'De goblin merchant heeft als koopwaard een zwaard en een schild, elk voor 1 ruppee.')

    while True:
        print(f'Je hebt {ruppees} ruppees.')
        print('1. Koop het schild (1 ruppee)')
        print('2. Koop het zwaard (1 ruppee)')
        keuze = input('Wat wil je doen? (1/2): ')

        if keuze == '1':
            if ruppees >= 1:
                player_defense += 1
                ruppees -= 1
                print('Je hebt het schild gekocht. Je defense is nu', player_defense)
                return 'schild', player_defense, player_attack, ruppees
            else:
                print('Je hebt niet genoeg ruppees om het schild te kopen.')
        elif keuze == '2':
            if ruppees >= 1:
                player_attack += 2
                ruppees -= 1
                print('Je hebt het zwaard gekocht. Je attack is nu', player_attack)
                return 'zwaard', player_defense, player_attack, ruppees
            else:
                print('Je hebt niet genoeg ruppees om het zwaard te kopen.')



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



