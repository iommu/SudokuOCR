#!/bin/bash

# {create .xml files from lableImg}
# mv ./*.xml files
mv ./images/*.xml ./annotations

# create proper directory structure
python3 ./xml_to_dir.py -in-xml annotations -in-img images -out data  

# run retrain script
python3 retrain.py --image_dir ./data