import math


def part2():
    with open("input.txt") as file:
        nums_list = []
        content = file.readlines()
        lines = [line.replace("\n", "") for line in content]
        calc_num = []
        _next = False
        for idy in range(len(lines[0])):
            num = ""
            for idx in range(len(lines)):
                symbol = lines[idx][len(lines[0]) - idy - 1]
                if symbol.isdigit():
                    num += symbol
                elif symbol in ["+", "*"]:
                    _next = True
            if num.isdigit():
                calc_num.append(int(num))
            if _next:
                nums_list.append(calc_num)
                calc_num = []
                _next = False
        operations = [op for op in lines[-1].split(" ")[::-1] if op in ["+", "*"]]
        res = 0
        for idx, nums in enumerate(nums_list):
            if operations[idx] == "+":
                res += sum(nums)
            else:
                res += math.prod(nums)
        print(res)

part2()