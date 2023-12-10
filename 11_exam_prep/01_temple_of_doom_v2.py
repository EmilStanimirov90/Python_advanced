from collections import deque

tools = deque([int(x) for x in input().split()])
subs = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while True:
    if not tools or not subs:
        break
    if not challenges:
        break

    tool = tools.popleft()
    sub = subs.pop()
    result = tool * sub
    for c in challenges:
        if c == result:
            challenges.remove(c)
            break

    else:
        tool += 1
        tools.append(tool)
        sub -= 1
        if sub > 0:
            subs.append(sub)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if subs:
    print(f"Substances: {', '.join([str(x) for x in subs])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
