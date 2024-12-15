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


def test_grid_with_4_decorations(test_grid_9):  # type: ignore
    # Given the expected result and the test_grid
    expected_result = 9

    # When finding the largest cluster
    result = largest_cluster(test_grid_9)

    # Then it must match with the expected result
    assert result == expected_result


def test_grid_just_ones(test_full_grid):  # type: ignore
    # Given the expected result and the full grid
    expected_result = 4

    # When finding the largest cluster
    result = largest_cluster(test_full_grid)

    # Then the result is the expected
    assert result == expected_result


def test_grid_without_decoration(test_grid_0):  # type: ignore
    # Given the default grid and the expected value
    expected_value = 0

    # When finding the size of the biggest grid
    result = largest_cluster(test_grid_0)

    # Then an exception is raise
    assert expected_value == result


def test_grid_single_row(test_single_row):  # type: ignore
    # Given the default grid and the expected value
    expected_value = 5

    # When finding the size of the biggest grid
    result = largest_cluster(test_single_row)

    # Then an exception is raise
    assert expected_value == result


def test_grid_full_row(test_full_row):  # type: ignore
    # Given the expected result and conftest
    expected_result = 5

    # When calculating the grid
    result = largest_cluster(test_full_row)

    # Then the result must match
    assert expected_result == result


def test_grid_single_column(test_single_column):  # type: ignore
    # Given the expected result and conftest
    expected_result = 5

    # When calculating the grid
    result = largest_cluster(test_single_column)

    # Then the result must match
    assert expected_result == result
