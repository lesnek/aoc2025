import math


def part1():
    with open("input.txt") as file:
        nums_list = []
        content = file.readlines()
        lines = [line.strip() for line in content]
        for line in lines[:-1]:
            nums = [num for num in line.split(" ") if num.isdigit()]
            nums_list.append(nums)
            print(nums_list)
        operations = [op for op in lines[-1].split(" ") if op in ["+", "*"]]
        print(operations)
        res = 0
        for idx in range(len(nums_list[0])):
            nums_to_calc = [int(num[idx]) for num in nums_list]
            if operations[idx] == "+":
                res += sum(nums_to_calc)
            else:
                res += math.prod(nums_to_calc)
        print(res)

part1()