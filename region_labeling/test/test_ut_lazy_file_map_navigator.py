import os

from ..map_navigators.lazy_file_map_navigator import LazyFileMapNavigator

def test_ut_in_memory_map_navigator_reset():
    print(os.getcwd())
    with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', 'simple_map.txt')) as map_navigator:
        pass
