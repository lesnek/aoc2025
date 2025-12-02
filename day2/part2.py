def part2():
    res = 0
    with open("input.txt", "r") as file:
        line = file.readlines()[0]
        ranges = [_line.split("-") for _line in line.split(",")]
    for _range in ranges:
        for num in range(int(_range[0]), int(_range[1]) + 1):
            str_num = str(num)
            for i in range(1, len(str_num)):
                if check_same(str_num, i):
                    res += num
                    break
    print(res)

def check_same(str_num: str, fraction: int):
    return all(str_num[:fraction] == str_num[fraction + i:fraction + i + fraction] for i in range(0, len(str_num) - fraction, fraction))



part2()