lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_broken = 0
sword_broken = 0
shield_broken = 0
armor_broken = 0

for count in range(1, lost_fights + 1):
    if count % 2 == 0:
        helmet_broken += 1
    if count % 3 == 0:
        sword_broken += 1
    if count % 6 == 0:
        shield_broken += 1
    if count % 12 == 0:
        armor_broken += 1

total_cost = helmet_price * helmet_broken + \
             + sword_price * sword_broken + \
             + shield_price * shield_broken + \
             + armor_price * armor_broken
print(f'Gladiator expenses: {total_cost:.2f} aureus')
