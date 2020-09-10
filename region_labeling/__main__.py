import os
import sys

from .map_navigators.lazy_file_map_navigator import LazyFileMapNavigator
from .region_detector import RegionDetector

if __name__ == '__main__':
    argc = len(sys.argv)
    help_msg = "Missing map file path. Example:\n$ python -m region_labeling <path_to_file_relative_to_cwd>\n"
    if argc < 2:
        sys.stderr.write(help_msg)
        sys.exit(-1)
    relative_map_file_path = sys.argv[1]

    with LazyFileMapNavigator(os.path.join(os.getcwd(), relative_map_file_path)) as map_navigator:
        region_detector = RegionDetector(map_navigator)
        print(region_detector.count_regions())
