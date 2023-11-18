from collections import deque

monsters = deque([int(x) for x in input().split(",")])
soldiers = [int(x) for x in input().split(",")]
monsters_killed = 0

while soldiers and monsters:

    soldier_attack = soldiers.pop()
    monster_defence = monsters.popleft()

    if soldier_attack >= monster_defence:
        monsters_killed += 1

        soldier_attack -= monster_defence

        if not soldiers and soldier_attack > 0:
            soldiers.append(soldier_attack)
        elif soldiers:
            soldiers[-1] += soldier_attack
    else:
        monster_defence -= soldier_attack
        monsters.append(monster_defence)

if not monsters:
    print("All monsters have been killed!")
if not soldiers:
    print("The soldier has been defeated.")


print(f"Total monsters killed: {monsters_killed}")
