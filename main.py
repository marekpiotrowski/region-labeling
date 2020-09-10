from map_navigators.in_memory_map_navigator import InMemoryMapNavigator
from region_detector import RegionDetector

if __name__ == '__main__':
    # map_navigator = InMemoryMapNavigator([[1, 1, 0, 0, 1], [0, 1, 0, 0, 1], [1, 0, 0, 0, 0]])
    # rd = RegionDetector(map_navigator)
    # rd.label_regions()

    mn1 = InMemoryMapNavigator([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0, 0, 0, 0, 0],
                                [1, 1, 1, 0, 0, 0, 1, 0, 0],
                                [1, 1, 0, 0, 0, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                                [1, 1, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 1, 1, 0, 0]])
    rd2 = RegionDetector(mn1)
    rd2.label_regions()
