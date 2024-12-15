from random import SystemRandom

VERT = 10
HORI = 10


def _populate_cells() -> list[int]:
    return [SystemRandom().randint(0, 1) for _ in range(10)]


def _create_grid() -> list[list[int]]:
    return [_populate_cells() for _ in range(10)]


def _get_coordinates_grid(grid: list[list[int]]) -> list[tuple[int, int]]:
    len_hor = len(grid[0])
    len_ver = len(grid)
    return [(i, j) for i in range(len_ver) for j in range(len_hor) if grid[i][j] != 0]


def _find_nodes(
    y: int,
    x: int,
    grid_coord: list[tuple[int, int]],
    visited: set[tuple[int, int]],
    coords: list[tuple[int, int]] = [],  # noqa: B006
    special: list[tuple[int, int]] = [],  # noqa: B006
) -> tuple[list[tuple[int, int]], set[tuple[int, int]]]:
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
        grids.append(coords)

    grids_filtered: list[set[tuple[int, int]]] = [set(_) for _ in grids]
    grids_filtered.sort(key=len, reverse=True)

    try:
        return len(grids_filtered[0])
    except IndexError:
        print(f"The grid had no decorations {grids_filtered=}")
        return 0


if __name__ == "__main__":
    grid = _create_grid()
    print(largest_cluster(grid))
