def part2():
    lines = open('input.txt').read().splitlines()
    boxes_amount = len(lines)
    edges = []
    for i, box_dir in enumerate(lines):
        x1, y1, z1 = [int(_dir) for _dir in box_dir.split(',')]
        for j, second_box_dir in enumerate(lines[i + 1:]):
            x2, y2, z2 = [int(_dir) for _dir in second_box_dir.split(',')]
            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1
            euklid_dist = dx ** 2 + dy ** 2 + dz ** 2
            edges.append((euklid_dist, i, j + i + 1))
    edges.sort()

    def find_root(x):
        if x != parent[x]:
            parent[x] = find_root(parent[x])
        return parent[x]

    def union(_a, _b):
        _a, _b = find_root(_a), find_root(_b)
        if _a == _b:
            return 0
        parent[_b] = _a
        size[_a] += size[_b]
        return size[_a]

    parent = list(range(boxes_amount))
    size = [1] * boxes_amount
    k = 0
    while True:
        _, a, b = edges[k]
        if union(a, b) == boxes_amount:
            break
        k += 1

    x1 = int(lines[a].split(',')[0])
    x2 = int(lines[b].split(',')[0])
    print('Part 2 :', x1 * x2)


part2()
