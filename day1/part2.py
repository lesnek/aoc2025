def part2():
    wheel = 100
    start = 50
    result = 0
    with open("day1.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]
    for line in lines:
        distance = int(line[1:])
        if line.startswith("L"):
            result += (start - 1) // wheel - (start - distance - 1) // wheel
            start -= distance
        else:
            result += (start + distance) // wheel - start // wheel
            start += distance
        start = start % wheel
        print(start)

    print(result)


part2()