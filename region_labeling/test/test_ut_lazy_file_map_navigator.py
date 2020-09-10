import os

from ..map_navigators.lazy_file_map_navigator import LazyFileMapNavigator


def test_ut_in_memory_map_navigator_move_right():
    with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', 'simple_map.txt')) as map_navigator:
        map_navigator.move_right_with_wrapping()
        map_navigator.move_right_with_wrapping()
        assert map_navigator.get_neighborhood() == [[0,0,0], [1,1]]


def test_ut_in_memory_map_update_element():
    with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', 'simple_map.txt')) as map_navigator:
        map_navigator.move_right_with_wrapping()
        map_navigator.move_right_with_wrapping()
        map_navigator.update_current_element(100)

        assert map_navigator.get_neighborhood() == [[0, 0, 0], [1, 100]]


def test_ut_in_memory_map_update_element_next_row():
    with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', 'simple_map.txt')) as map_navigator:
        map_navigator.move_right_with_wrapping()
        map_navigator.move_right_with_wrapping()
        map_navigator.update_current_element(100)
        assert map_navigator.get_neighborhood() == [[0, 0, 0], [1, 100]]
        for i in range(8):
            map_navigator.move_right_with_wrapping()
        assert map_navigator.get_neighborhood() == [[0, 1, 100], [0, 1]]
