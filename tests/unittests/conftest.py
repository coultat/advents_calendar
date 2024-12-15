import pytest


@pytest.fixture
def test_grid_30() -> list[list[int]]:
    return [
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]


@pytest.fixture
def test_grid_13() -> list[list[int]]:
    return [
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    ]


@pytest.fixture
def test_grid_9() -> list[list[int]]:
    return [[0, 0, 0, 0], [0, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1]]


@pytest.fixture
def test_grid_1_cell() -> list[list[int]]:
    return [[1]]

@pytest.fixture
def test_grid_0() -> list[list[int]]:
    return [[0, 0], [0, 0]]


@pytest.fixture
def test_full_grid() -> list[list[int]]:
    return [[1, 1], [1, 1]]


@pytest.fixture
def test_full_row() -> list[list[int]]:
    return [
        [
            1,
            1,
            1,
            1,
            1,
        ],
        [0, 0, 0, 0, 0],
    ]


@pytest.fixture
def test_single_row() -> list[list[int]]:
    return [[1, 1, 1, 1, 1]]


@pytest.fixture
def test_single_column() -> list[list[int]]:
    return [[1], [1], [1], [1], [1]]
