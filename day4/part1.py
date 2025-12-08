def part1():
    res = 0
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        rows = len(lines)
        cols = len(lines[0]) if rows > 0 else 0
        
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] == '@':
                    adjacent_count = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] == '@':
                            adjacent_count += 1
                    
                    if adjacent_count < 4:
                        res += 1
        
        print(res)

part1()