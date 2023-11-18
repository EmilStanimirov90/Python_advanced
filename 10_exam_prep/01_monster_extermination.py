from collections import deque

monster_armor = deque([int(x) for x in input().split(",")])
soldier_strikes = [int(x) for x in input().split(",")]
monsters_killed = 0
while True:
    if not soldier_strikes:
        print("The soldier has been defeated.")
        break
    if not monster_armor:
        print("All monsters have been killed!")
        break

    current_monster_armor = monster_armor.popleft()
    current_soldier_strike = soldier_strikes.pop()

    if current_soldier_strike > current_monster_armor:

        if soldier_strikes:
            soldier_strikes[-1] += current_soldier_strike - current_monster_armor
        else:
            soldier_strikes.append(current_soldier_strike - current_monster_armor)
        monsters_killed += 1
    elif current_soldier_strike == current_monster_armor:
        monsters_killed += 1
    elif current_monster_armor > current_soldier_strike:
        monster_armor.append(current_monster_armor - current_soldier_strike)

print(f"Total monsters killed: {monsters_killed}")
