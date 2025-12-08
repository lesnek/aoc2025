def part2():
    with open("input.txt") as file:
        content = file.read().strip()
        ranges_section = content.split("\n\n")[0]

        ranges = []
        for line in ranges_section.split("\n"):
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

        ranges.sort()
        merged = []
        for start, end in ranges:
            if merged and start <= merged[-1][1] + 1:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))
        total = sum(end - start + 1 for start, end in merged)

        print(total)

part2()