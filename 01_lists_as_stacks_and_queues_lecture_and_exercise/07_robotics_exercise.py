from collections import deque

products_queue = deque()
robots = []
robots_data = input().split(";")
hours, minutes, seconds = [int(x) for x in input().split(":")]
starting_time_seconds = hours * 3600 + minutes * 60 + seconds


for robot in robots_data:
    robot_name, processing_time = robot.split("-")
    busy_until_time = 0
    robots.append({'name': robot_name, 'data': [int(processing_time), busy_until_time]})


while True:
    product = input()
    if product == "End":
        break
    products_queue.append(product)

while products_queue:
    starting_time_seconds += 1
    current_product = products_queue.popleft()
    is_taken = False

    for robot in robots:
        if robot['data'][1] <= starting_time_seconds:
            robot['data'][1] = starting_time_seconds + robot["data"][0]
            h = starting_time_seconds // 3600
            m = (starting_time_seconds % 3600) // 60
            s = (starting_time_seconds % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break

    if not is_taken:
        products_queue.append(current_product)
