#!/bin/sh

if [ "$#" -ne 1 ]; then
  echo "Usage: ./count_regions.sh <map_file_path_relative_to_cwd>"
  exit 1
fi

python3 -m region_labeling "$@"