from collections import defaultdict


def part2():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    start_col = None
    for line in lines:
        if 'S' in line:
            start_col = line.index('S')
            break
    timeline_counts = defaultdict(int)
    timeline_counts[start_col] = 1

    for line in lines:
        next_counts = defaultdict(int)

        for col, count in timeline_counts.items():
            if col < 0 or col >= len(line):
                continue

            char = line[col]
            if char == '^':
                next_counts[col - 1] += count
                next_counts[col + 1] += count
            else:
                next_counts[col] += count

        timeline_counts = next_counts
    print(sum(timeline_counts.values()))

part2()