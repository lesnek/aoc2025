def part1():
    wheel = 100
    start = 50
    result = 0
    with open("day1.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]
    for line in lines:
        if line.startswith("L"):
            start -= int(line[1:])
        else:
            start += int(line[1:])
        start = start % wheel
        if start == 0:
            result += 1
    print(result)


part1()