import tensorflow as tf

# # Create and compute a TensorFlow operation
# x = tf.constant([1, 2, 3])
# y = tf.square(x)
# z = tf.reduce_sum(y)

# # Print the result
# print(z.numpy())  # Convert the TensorFlow tensor to a NumPy array
from tensorflow import keras

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout( 0.2),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)