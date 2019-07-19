#!/bin/bash

# generate the combined CSV
python3 ./xml_to_csv.py -in annotations -out data/labels.csv  

# convert csv to tfrecord
python3 ./generate_tfrecord.py -in data/labels.csv -out data/train.record
# generate test.record (same as train for now)
python3 ./generate_tfrecord.py -in data/labels.csv -out data/test.record