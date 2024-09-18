import tensorflow as tf

print("TensorFlow version:", tf.__version__)

# Check if TensorFlow is built with CUDA (GPU support)
print("Is GPU available?", tf.config.list_physical_devices('GPU'))
