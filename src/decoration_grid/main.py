from random import randint
#import numpy as np

VERT = 10
HORI = 10


def _populate_cells() -> list[int]:
    return [randint(0, 1) for _ in range(10)]


def _create_grid() -> list[list[int]]:
    return [_populate_cells() for _ in range(10)]


def _get_coordinates_grid(grid):
    grid_coord = list()
    for i in range(HORI):
        for j in range(VERT):
            if grid[i][j] == 0:
                continue
            grid_coord.append((i, j))
    return grid_coord


def _find_nodes(y, x, grid_coord, visited, coords=list(), special=list()):
    if 0 <= y < VERT and (y - 1, x) in grid_coord and (y - 1, x) not in visited:
        if (y, x) not in special:
            special.append((y, x))
        visited.add((y - 1, x))
        coords.append((y - 1, x))
        coords, visited = _find_nodes(y - 1, x, grid_coord, visited, coords, special)

    elif 0 <= x < HORI and (y, x + 1) in grid_coord and (y, x + 1) not in visited:
        if (y, x) not in special:
            special.append((y, x))
        visited.add((y, x + 1))
        coords.append((y, x + 1))
        coords, visited = _find_nodes(y, x + 1, grid_coord, visited, coords, special)

    elif 0 <= x < HORI and (y, x - 1) in grid_coord and (y, x - 1) not in visited:
        if (y, x) not in special:
            special.append((y, x))
        visited.add((y, x - 1))
        coords.append((y, x - 1))
        coords, visited = _find_nodes(y, x - 1, grid_coord, visited, coords, special)

    elif 0 <= y < VERT and (y + 1, x) in grid_coord and (y + 1, x) not in visited:
        if (y, x) not in special:
            special.append((y, x))
        visited.add((y + 1, x))
        coords.append((y + 1, x))
        coords, visited = _find_nodes(y + 1, x, grid_coord, visited, coords, special)

    if special:
        y, x = special.pop()
        coords, visited = _find_nodes(y, x, grid_coord, visited, coords, special)
    return coords, visited


def largest_cluster(grid: list[list[int]]) -> int:
    grid_coord = _get_coordinates_grid(grid)
    visited = set()
    grids = []
    for node in grid_coord:
        coords = [node]
        visited.add(node)
        y, x = node
        coords, visited = _find_nodes(y, x, grid_coord, visited, coords)
        print(f"{coords=}")
        grids.append(coords)

    grids = [set(grida) for grida in grids]
    grids.sort(key=len, reverse=True)
    try:
        grid_size = len(grids[0])
    except IndexError:
        print(f"The grid had no decorations {grid=}")
        return 0
    return grid_size


if __name__ == "__main__":
    grid = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
           [1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
           [1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
           [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(largest_cluster(grid))
