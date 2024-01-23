import random
import time
import math
# to do alle exit weg halen
#####################################################################
def kamer_2(ruppees):
    print("Kamer 2\n")
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een steen vast.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')

    getal1 = random.randint(10, 25)
    getal2 = random.randint(-5, 75)
    som = getal1 + getal2

    print(f'Daarboven zie je een som staan {getal1}+{getal2}=?')
    antwoord = int(input('Wat toets je in?'))

    if antwoord == som:
        print('Het standbeeld laat een ruppee vallen en je pakt het op.')
        ruppees += 1
        print(f"je hebt nu {ruppees} ruppees")
    else:
        print(f'Helaas, het correcte antwoord was {som}. Er gebeurt niets....')

    print('Je ziet een deur achter het standbeeld.')
    print('')
    time.sleep(1)
    return ruppees
#####################################################################
def kamer_3(player_defense, player_attack, ruppees):
    # dat je meredere items kunt kopen tot je 0 rupppees en dat je ook de optie krijgt om niks te kopen
    print("Kamer 3\n")
    print(f'Je loopt nu binnen de volgende kamer en vind daar binnen een goblin merchant')
    print(f'Je hebt {ruppees} ruppees.')
    if ruppees == 1:
        print("wilt u een zwaard of schild kopen? voor ruppee")
    elif ruppees > 1:
        print("wilt u een zwaard en schild kopen? voor 2 ruppee")

    keuze = input('Wat wil je doen? (schild, zwaard, beide, sleutel): ')

    if keuze == 'schild':
        if ruppees >= 1:
            player_defense += 1
            ruppees -= 1
            item = 'schild'
            print(f'Je hebt het schild gekocht. Je defense is nu {player_defense}.')
            return item, player_defense, player_attack, ruppees
        else:
            print('Je hebt niet genoeg ruppees om het schild te kopen.')
    elif keuze == 'zwaard':
        if ruppees >= 1:
            player_attack += 2
            ruppees -= 1
            item = 'zwaard'
            print(f'Je hebt het zwaard gekocht. Je attack is nu {player_attack}.')
            return item, player_defense, player_attack, ruppees
    elif keuze == 'beide':
        if ruppees >= 2:
            player_attack += 2
            player_defense += 1
            ruppees -= 2
            item = 'zwaard', 'schild'
            print(f'Je hebt een zwaard en schild gekocht. Je attack is nu {player_attack} en je defense is nu {player_defense}.')
            return item, player_defense, player_attack, ruppees
    elif keuze == 'sleutel':
        if ruppees >= 1:
            ruppees -= 1
            item = 'sleutel'
            print(f'Je hebt de sleutel voor de schatkist gekocht..')
            return item, player_defense, player_attack, ruppees
    else:
        print('Je hebt niet genoeg ruppees om iets te kopen.')
#####################################################################
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

#####################################################################
def kamer_7(ruppees):
    print("Kamer 7\n")
    een_op_tien = random.randint(1, 10)
    # moet de kans 90%
    if een_op_tien == 1:
        ruppees += 1
        print("Je vindt in de volgende kamer een steen")
        print("de naam van de steen is ruppee en je pakt het op")
    print(f"Je hebt nu in totaal {ruppees} ruppees.")
    print("Op naar de volgende kamer\n")
    return ruppees
#####################################################################
def kamer_4(player_defense, player_attack, player_health):
    print("Kamer 4\n")
    bandit_attack = 2
    bandit_defense = 0
    bandit_health = 3

    print("In kamer 4 vind je een treasure bandit.\n")

    enemy_hit_damage = (bandit_attack - player_defense)
    if enemy_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de bandit, hij kan je geen schade doen.')
    else:
        enemy_attack_amount = math.ceil(player_health / enemy_hit_damage)
        
        player_hit_damage = (player_attack - bandit_defense)
        player_attack_amount = math.ceil(bandit_health / player_hit_damage)

        if player_attack_amount < enemy_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de bandit.')
            print(f'Je health is nu {player_health - enemy_attack_amount}.')
        else:
            print('Helaas is de bandit te sterk voor je.')
            print('Game over.')
            exit()

    print('')
    time.sleep(1)
#####################################################################
def kamer_5():
    print("Kamer 5\n")
    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
#####################################################################
def kamer_8(ruppees, player_health):
    print("Welkom bij de gokmachine!\n")
    input("Druk op Enter om de dobbelstenen te gooien")

    dobbelsteen1 = random.randint(1, 6)
    dobbelsteen2 = random.randint(1, 6)

    totaal = dobbelsteen1 + dobbelsteen2

    print(f"\nJe hebt {dobbelsteen1} en {dobbelsteen2} gegooid. Totaal: {totaal}\n")

    if totaal > 7:
        verdubbellen = ruppees * 2
        ruppees = verdubbellen
        print(f"Gefeliciteerd! Je hebt gewonnen en je ruppees zijn verdubbeld naar {ruppees}.")
    elif totaal < 7:
        player_health -= 1
        print(f"Helaas! Je hebt verloren en verliest 1 health. Je health is nu {player_health}.")
    elif totaal == 7:
        verdubbellen = ruppees * 2
        ruppees = verdubbellen
        player_health -= 1
        print(f"Je hebt zowel gewonnen als verloren. Je ruppees zijn verdubbeld naar {ruppees} en je verliest 1 health. Je health is nu {player_health}.")

    return ruppees, player_health
#####################################################################
def kamer_9(player_defense, player_health):
    print("er zit hier een betovering in deze kamer, de betovering kan meer defense of meer health geven")
    boost = ["defense","health"]
    betovering = random.choice(boost)
    print(f"je hebt de {betovering} betovering gekregen")
    if betovering == 'defense':
        player_defense += 1
        print(f"je defense is nu {player_defense}")
    else:
        player_health += 2
        print(f"je health is nu {player_health}")
    return player_defense, player_health
#####################################################################
def kamer_10(player_defense, player_attack, player_health):
    print("Kamer 4\n")
    boss_attack = 3
    boss_defense = 1
    boss_health = 5

    print("In kamer 10 vind je de boss.\n")

    enemy_hit_damage = (boss_attack - player_defense)
    if enemy_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de boss, hij kan je geen schade doen.')
    else:
        enemy_attack_amount = math.ceil(player_health / enemy_hit_damage)
        
        player_hit_damage = (player_attack - boss_defense)
        player_attack_amount = math.ceil(boss_health / player_hit_damage)

        if player_attack_amount < enemy_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de boss.')
            print(f'Je health is nu {player_health - enemy_attack_amount}.')
        else:
            print('Helaas is de boss te sterk voor je.')
            print('Game over.')
            exit()

    print('')
    time.sleep(1)