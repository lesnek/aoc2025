def part1():
    res = 0
    with open("input.txt", "r") as file:
        line = file.readlines()[0]
        ranges = [_line.split("-") for _line in line.split(",")]
    for _range in ranges:
        for num in range(int(_range[0]), int(_range[1]) + 1):
            str_num = str(num)
            if len(str_num) % 2 == 0:
                left = str_num[:len(str_num) // 2]
                right = str_num[len(str_num) // 2:]
                if left == right:
                    res += num
    print(res)

part1()