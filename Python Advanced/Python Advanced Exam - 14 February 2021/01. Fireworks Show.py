from collections import deque

effects = deque(map(int, input().split(', ')))
powers = list(map(int, input().split(', ')))
palm = 0
willow = 0
crossette = 0

while effects and powers:
    if palm == 3 and willow == 3 and crossette == 3:
        break
    if effects[0] <= 0:
        effects.popleft()
        continue
    if powers[-1] <= 0:
        powers.pop()
        continue
    effect = effects.popleft()
    power = powers.pop()
    result = effect + power
    if result % 3 == 0 and result % 5 == 0:
        crossette += 1
    elif result % 3 == 0 and result % 5 != 0:
        palm += 1
    elif result % 3 != 0 and result % 5 == 0:
        willow += 1
    else:
        powers.append(power)
        effects.append(effect - 1)

if palm >= 3 and willow >= 3 and crossette >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")

if powers:
    print(f"Explosive Power left: {', '.join(map(str, powers))}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
