m, n = map(int, input().split())
bomb = int(input())
bomb_positions = set()

for _ in range(bomb):
    x, y = map(int, input().split())
    bomb_positions.add((x - 1, y - 1))

matrice = [[0] * n for _ in range(m)]

for x, y in bomb_positions:
    matrice[x][y] = '*'

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(m):
    for j in range(n):
        if matrice[i][j] == '*':
            continue
        bomb_count = 0
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n and matrice[ni][nj] == '*':
                bomb_count += 1
        matrice[i][j] = bomb_count

for row in matrice:
    print(' '.join(str(cell) for cell in row))
