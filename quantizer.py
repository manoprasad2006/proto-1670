import tensorflow as tf

# Load the original TensorFlow Lite model
converter = tf.lite.TFLiteConverter.from_saved_model('C:/Users/Mano Prasad/OneDrive/Desktop/orprpe/model.tflite')

# Set quantization options
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Use default optimization settings

# Convert to quantized TFLite model
quantized_tflite_model = converter.convert()

# Save the quantized model
with open("quantized_model.tflite", "wb") as f:
    f.write(quantized_tflite_model)

