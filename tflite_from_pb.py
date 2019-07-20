import tensorflow as tf

graph_def_file = "/tmp/output_graph.pb"
input_arrays = ["/tmp/output_labels.txt"]
output_arrays = ["MobilenetV1/Predictions/Softmax"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("sudoku.tflite", "wb").write(tflite_model)