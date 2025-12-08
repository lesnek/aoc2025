def part1():
    with open("input.txt") as file:
        content = file.read().strip()
        ranges_section, ids_section = content.split("\n\n")
        
        ranges = []
        for line in ranges_section.split("\n"):
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        
        ingredient_ids = [int(line) for line in ids_section.split("\n")]
        
        fresh_count = 0
        for ingredient_id in ingredient_ids:
            is_fresh = any(start <= ingredient_id <= end for start, end in ranges)
            if is_fresh:
                fresh_count += 1
        
        print(fresh_count)

part1()