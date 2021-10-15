grid = [[0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]]

rows = len(grid)
cols = len(grid[0])

visited = []
for r in range(rows):
    visited.append([0] * len(grid[r]))


island_size = {}


def flood_fill(x, y, color):
    grid[x][y] = color
    visited[x][y] = 1
    island_size[color] += 1
    coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in coordinates:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols:
            if grid[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                flood_fill(new_x, new_y, color)


# color island and count the size of the island
def color_and_calculate_size_of_islands():
    island_colors = 0
    island_size[island_colors] = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and visited[i][j] == 0:
                island_colors += 1
                island_size[island_colors] = 0
                flood_fill(i, j, island_colors)


def make_largest_island():
    #color islands and get island sizes

    color_and_calculate_size_of_islands()
    # get max island size before merge
    max_island_size = max(island_size.keys())
    # iterate over matrix and ,if cell = 0 get sizes of the 4 directions by color
    for ii in range(rows):
        for jj in range(cols):
            # if cell is not an island
            if grid[ii][jj] == 0:
                # get 4 directions and insert color of the adj unique islands
                coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                nei_colors = set()
                for dx, dy in coordinates:
                    new_i = ii + dx
                    new_j = jj + dy
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        nei_colors.add(grid[new_i][new_j])
                # iterate over unique islands and merge the size + 1
                this_island_size = 1
                for color in nei_colors:
                    this_island_size += island_size[color]
                #check if new island is the largest island
                max_island_size = max(max_island_size, this_island_size)
    return max_island_size

print(grid)
print(make_largest_island())
