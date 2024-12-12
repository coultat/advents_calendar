import pytest

from src.decoration_grid.main import largest_cluster


def test_grid_with_30_decorations(test_grid_30):  # type: ignore
    # Given the default grid and the expected result
    expected_result = 30

    # When finding the size of the biggest grid
    largest_grid = largest_cluster(test_grid_30)

    # Then the result must match
    assert expected_result == largest_grid


def test_grid_with_13_decorations(test_grid_13):  # type: ignore
    # Given the default grid and the expected result
    expected_result = 13

    # When finding the size of the biggest grid
    largest_grid = largest_cluster(test_grid_13)

    # Then the result must match with the expected result
    assert largest_grid == expected_result


def test_grid_without_decoration(test_grid_0):  # type: ignore
    # Given the default grid

    # When finding the size of the biggest grid

    # Then an exception is raise
    with pytest.raises(IndexError):
        _ = largest_cluster(test_grid_0)
