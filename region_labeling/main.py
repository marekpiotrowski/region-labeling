from .map_navigators.in_memory_map_navigator import InMemoryMapNavigator
from .region_detector import RegionDetector

if __name__ == '__main__':
    # map_navigator = InMemoryMapNavigator([[1, 1, 0, 0, 1], [0, 1, 0, 0, 1], [1, 0, 0, 0, 0]])
    # rd = RegionDetector(map_navigator)
    # rd.count_regions()

    # mn1 = InMemoryMapNavigator([[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                             [0, 1, 0, 0, 0, 0, 0, 0, 0],
    #                             [1, 1, 1, 0, 0, 0, 1, 0, 0],
    #                             [1, 1, 0, 0, 0, 1, 1, 1, 0],
    #                             [0, 0, 0, 0, 0, 1, 1, 0, 0],
    #                             [0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                             [1, 1, 0, 0, 0, 0, 0, 0, 0],
    #                             [0, 0, 0, 0, 0, 1, 1, 0, 0]])
    # rd1 = RegionDetector(mn1)
    # print(rd2.count_regions())

    mn2 = InMemoryMapNavigator([[1, 0, 1, 0, 1],
                                [0, 1, 0, 1, 0],
                                [1, 0, 1, 0, 1],
                                [0, 1, 0, 1, 0],
                                [1, 0, 1, 0, 1]])
    rd2 = RegionDetector(mn2)
    print(rd2.count_regions())
