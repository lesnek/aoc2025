def part1():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        res = 0
        for line in lines:
            biggest = 0
            biggest2 = 0
            pos_big = 0
            for idx, num in enumerate(line[:-1]):
                if int(num) > biggest:
                    biggest = int(num)
                    pos_big = idx
            for num in line[pos_big + 1:]:
                if int(num) > biggest2:
                    biggest2 = int(num)
            print(int(f"{biggest}{biggest2}"))
            res += int(f"{biggest}{biggest2}")
        print(res)

part1()