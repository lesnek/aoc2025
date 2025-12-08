def part2():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        rows = len(lines)
        cols = len(lines[0]) if rows > 0 else 0
        
        grid = [list(line) for line in lines]
        
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        total_removed = 0
        
        while True:
            accessible = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == '@':
                        adjacent_count = 0
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                                adjacent_count += 1
                        
                        if adjacent_count < 4:
                            accessible.append((r, c))
            
            if not accessible:
                break
            
            for r, c in accessible:
                grid[r][c] = '.'
            
            total_removed += len(accessible)

        print(total_removed)


part2()