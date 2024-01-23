import time, math, random
from functions import *

player_attack = 1
player_defense = 0
player_health = 3
item = None
ruppee = 0

# === [kamer 1] === #
print("Kamer 1\n")
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
print("Kamer 7\n")
print("Je vindt in de volgende kamer een steen")
print("de naam van de steen is ruppee en je pakt het op")
ruppee += 1
print(f"je hebt nu in totaal {ruppee}")
print("op naar de volgende kamer\n")

print("je kunt nu 2 richtingen kiezen")
print("je kunt door gaan via kamer 2 of gelijk gaan naar kamer 3")
kamer2_3 = input("welke kamer wil je naar toe gaan")
if kamer2_3 == "3":
    item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)
elif kamer2_3 == "2":
    print("")


# === [kamer 2] === #
print("Kamer 2\n")
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')

getal1 = random.randint(10, 25)
getal2 = random.randint(-5, 75)
som = getal1 + getal2

print(f'Daarboven zie je een som staan {getal1}+{getal2}=?')
antwoord = int(input('Wat toets je in?'))

if antwoord == som:
    print('Het standbeeld laat de sleutel vallen en je pakt het op.')
else:
    print(f'Helaas, het correcte antwoord was {som}. Er gebeurt niets....')

print('Je ziet een deur achter het standbeeld.')
print('')
time.sleep(1)

print('Je kan nu kiezen om naar kamer 3 tegaan of naar kamer 6 via kamer 6 kom je weer uit op kamer 3.')
kamer = input('Kies naar welke kamer je wilt gaan (6 of 3): ')

if kamer == "6":
    # === [kamer 6] === #
    kamer_6()

else:
    item, player_defense, player_attack, ruppee = kamer_3(player_defense, player_attack, ruppee)

# === [kamer 4] === #
print("Kamer 4\n")
bandit_attack = 2
bandit_defense = 0
bandit_health = 3

print("in kamer 4 vind je een treasure bandit\n")

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

# === [kamer 5] === #
print("Kamer 5\n")
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')