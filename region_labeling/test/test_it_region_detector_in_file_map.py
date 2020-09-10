import pytest
import os

from ..map_navigators.lazy_file_map_navigator import LazyFileMapNavigator
from ..region_detector import RegionDetector
from ..config import Config


class TestData(object):
    # list of tuples, where first param is the filename, second param is expected number of regions
    all_examples = [('simple_map_pdf.txt', 4), ('map_1000x1000.txt', 1), ('map_algo_doc.txt', 3)]


@pytest.mark.parametrize("file_with_output", TestData.all_examples)
def test_it_region_detector_lazy_file_map(file_with_output):
    with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', file_with_output[0])) as map_navigator:
        region_detector = RegionDetector(map_navigator)
        assert region_detector.count_regions() == file_with_output[1]


def test_it_region_detector_file_does_not_exist():
    Config.validate = True
    with pytest.raises(Exception) as excinfo:
        with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', 'abc.txt')) as map_navigator:
            pass
    assert "Problem opening the map file" in str(excinfo.value)


def test_it_region_detector_file_is_empty():
    Config.validate = True
    with pytest.raises(Exception) as excinfo:
        with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', 'empty.txt')) as map_navigator:
            pass
    assert "Map file is empty" in str(excinfo.value)


def test_it_region_detector_file_cotains_not_allowed_symbols():
    Config.validate = True
    with pytest.raises(Exception) as excinfo:
        with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', 'incorrect_map.txt')) as map_navigator:
            pass
    assert "Incorrect entries in map file" in str(excinfo.value)