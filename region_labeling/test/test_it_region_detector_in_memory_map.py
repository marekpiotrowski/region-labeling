import pytest

from ..map_navigators.in_memory_map_navigator import InMemoryMapNavigator
from ..region_detector import RegionDetector

class TestData(object):
    # lecture_example = []
    pdf_example = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0, 1, 0, 0],
                    [1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0, 0]]
    hardest_possible_small_dim = [[1, 0, 1, 0, 1],
                                [0, 1, 0, 1, 0],
                                [1, 0, 1, 0, 1],
                                [0, 1, 0, 1, 0],
                                [1, 0, 1, 0, 1]]

    # list of tuples, where first param is the array, second param is expected number of regions
    all_examples = [(pdf_example, 4), (hardest_possible_small_dim, 1)]


@pytest.mark.parametrize("static_example", TestData.all_examples)
def test_it_region_detector_in_memory_map_static_example(static_example):
    map_navigator = InMemoryMapNavigator(static_example[0])
    region_detector = RegionDetector(map_navigator)
    assert region_detector.count_regions() == static_example[1]


@pytest.mark.skip(msg="Long test. Enable later.")
def test_it_region_detector_in_memory_map_hardest_possible_large_dim():
    dim = 1000
    map_2d_array = []
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append((j + ((i + 1) % 2)) % 2)
        map_2d_array.append(row)

    map_navigator = InMemoryMapNavigator(map_2d_array)
    region_detector = RegionDetector(map_navigator)
    assert region_detector.count_regions() == 1