grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]]

rows = len(grid)
cols = len(grid[0])
visited = []
for r in range(rows):
    visited.append([0] * len(grid[r]))


def flood_fill(x, y, color):
    grid[x][y] = color
    visited[x][y] = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols:
            if grid[new_x][new_y] == 1 and not visited[new_x][new_y]:
                flood_fill(new_x, new_y, color)


def color_islands():
    color_number = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and visited[i][j] == 0:
                color_number += 1
                flood_fill(i, j, color_number)


color_islands()
print(grid)
