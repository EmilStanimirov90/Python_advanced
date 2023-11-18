from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    popped_tool = tools.popleft()
    popped_substance = substances.pop()
    result = popped_tool * popped_substance

    if result in challenges:
        challenges.remove(result)
    else:
        popped_tool += 1
        tools.append(popped_tool)
        popped_substance -= 1
        if popped_substance > 0:
            substances.append(popped_substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

elif not tools or not substances and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
