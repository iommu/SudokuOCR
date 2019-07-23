#!/bin/bash

# {create .xml files from lableImg}
# mv ./*.xml files
mv ./images/*.xml ./annotations

# create proper directory structure
python3 ./xml_to_dir.py -in-xml annotations -in-img images -out data  

# run retrain script
python3 retrain.py --image_dir ./data

# convert to tflite from .pb
toco \
  --graph_def_file=/tmp/output_graph.pb \
  --output_file=./output/output_graph.tflite \
  --input_array=Placeholder \
  --output_array=final_result

mv  /tmp/output_labels.txt ./output/labels.txt