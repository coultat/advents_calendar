from src.decoration_grid.main import largest_cluster


def test_grid_with_30_decorations(test_grid_30):  # type: ignore
    # Given the default grid and the expected result
    expected_result = 30

    # When finding the size of the biggest grid
    largest_grid = largest_cluster(test_grid_30)

    # Then the result must match
    assert expected_result == largest_grid



def test_new_lolailo(test_new_design):
    result = largest_cluster(test_new_design)
    print(f"////////{result}///")
    assert 1 == 1
