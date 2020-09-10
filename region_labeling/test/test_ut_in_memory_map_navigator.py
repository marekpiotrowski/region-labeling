from ..map_navigators.in_memory_map_navigator import InMemoryMapNavigator


def test_ut_in_memory_map_move_right():
    map_navigator = InMemoryMapNavigator([[1, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                                        [1, 1, 1, 0, 0, 0, 1, 0, 0],
                                        [1, 1, 0, 0, 0, 1, 1, 1, 0],
                                        [0, 0, 0, 0, 0, 1, 1, 0, 0],
                                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
                                        [1, 1, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 1, 1, 0, 0]])

    map_navigator.move_right_with_wrapping()
    map_navigator.move_right_with_wrapping()

    assert map_navigator.get_neighborhood() == [[0, 0, 0], [1, 0]]


def test_ut_in_memory_map_update_element():
    map_navigator = InMemoryMapNavigator([[1, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                                        [1, 1, 1, 0, 0, 0, 1, 0, 0],
                                        [1, 1, 0, 0, 0, 1, 1, 1, 0],
                                        [0, 0, 0, 0, 0, 1, 1, 0, 0],
                                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
                                        [1, 1, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 1, 1, 0, 0]])

    map_navigator.move_right_with_wrapping()
    map_navigator.move_right_with_wrapping()
    map_navigator.update_current_element(100)

    assert map_navigator.get_neighborhood() == [[0, 0, 0], [1, 100]]