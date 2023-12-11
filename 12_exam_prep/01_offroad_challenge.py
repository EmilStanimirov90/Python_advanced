from collections import deque

initial_fuel_seq = [int(x) for x in input().split()]
aci = deque([int(x) for x in input().split()])
altitudes = [int(x) for x in input().split()]
reached_altitudes = []
failed_altitudes = []
for number, altitude in enumerate(altitudes, 1):

    result = initial_fuel_seq.pop() - aci.popleft()
    if result >= altitude:
        reached_altitudes.append(number)
        failed_altitudes.append(number)
        print(f"John has reached: Altitude {number}")
    else:
        print(f"John did not reach: Altitude {number}")
        break

if len(reached_altitudes) == len(altitudes):
    print("John has reached all the altitudes and managed to reach the top!")
elif not reached_altitudes:
    print("John failed to reach the top.")
    print(f"John didn't reach any altitude.")
else:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join('Altitude ' + str(n) for n in reached_altitudes)}")
