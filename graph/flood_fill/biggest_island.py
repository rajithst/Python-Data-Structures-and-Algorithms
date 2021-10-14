grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]]

rows = len(grid)
cols = len(grid[0])
island_size = {}
visited = []
for i in range(rows):
    visited.append([0] * cols)


def flood_fill(x, y, color):
    visited[x][y] = 1
    grid[x][y] = color
    island_size[color] += 1
    coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in coordinates:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols:
            if grid[new_x][new_y] == 1 and not visited[new_x][new_y]:
                flood_fill(new_x, new_y, color)


def biggest_island():
    island_color = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and visited[i][j] == 0:
                island_color += 1
                island_size[island_color] = 0
                flood_fill(i, j, island_color)


biggest_island()
print(grid)
print(island_size)
