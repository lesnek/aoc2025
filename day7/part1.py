


def part1():
    with open("input.txt") as file:
        merges = 0
        content = file.readlines()
        lines = [line.strip() for line in content]
        score_list = [0 for _ in range(len(lines) - 1)]
        for line in lines:
            if sid := line.find("S"):
                if sid > 0:
                    score_list[sid] = 1
            truth_line = [0 if sym != "^" else 1 for sym in line]
            score = [a & b for a, b in zip(score_list, truth_line)]
            merges += sum(score)
            for idx, scr in enumerate(score):
                if scr == 1:
                    if scr >=1:
                        score_list[idx - 1] = 1
                    score_list[idx] = 0
                    if scr <= len(lines) - 1:
                        score_list[idx + 1] = 1
        print(merges)

part1()