def part2():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        res = 0
        for line in lines:
            biggest = create_biggest_12_digit_number(line)
            res += biggest
        print(res)

def create_biggest_12_digit_number(line: str) -> int:
    garbage = len(line) - 12
    best_nums = []
    for digit in line:
        while best_nums and garbage > 0 and best_nums[-1] < digit:
            best_nums.pop()
            garbage -= 1
        best_nums.append(digit)

    return int("".join(best_nums[:12]))

part2()
# 171518260283767