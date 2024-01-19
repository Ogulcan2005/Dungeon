import time, math, random

player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
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

# === [kamer 3] === #

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
    print(f'Het {item} geeft je een meer attack. Je attack is nu {player_attack}.')
print('Op naar de volgende deur.')
print("")
time.sleep(1)

# === [kamer 4] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
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

print("Na het gevecht met de zombie kom je een nieuwe vijand tegen in de zelfde kamer")

new_enemy_attack = 2
new_enemy_defense = 0
new_enemy_health = 3

enemy_hit_damage = (new_enemy_attack - player_defense)
if enemy_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de vijand, hij kan je geen schade doen.')
else:
    enemy_attack_amount = math.ceil(player_health / enemy_hit_damage)
    
    player_hit_damage = (player_attack - new_enemy_defense)
    player_attack_amount = math.ceil(new_enemy_health / player_hit_damage)

    if player_attack_amount < enemy_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de vijand.')
        print(f'Je health is nu {player_health - enemy_attack_amount}.')
    else:
        print('Helaas is de vijand te sterk voor je.')
        print('Game over.')
        exit()

print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')