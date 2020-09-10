import pytest
import os

from ..map_navigators.lazy_file_map_navigator import LazyFileMapNavigator
from ..region_detector import RegionDetector


def test_it_region_detector_lazy_file_map_pdf_example():
    with LazyFileMapNavigator(os.path.join(os.getcwd(), 'region_labeling', 'test', 'test_data', 'simple_map_pdf.txt')) as map_navigator:
        region_detector = RegionDetector(map_navigator)
        assert region_detector.count_regions() == 4
