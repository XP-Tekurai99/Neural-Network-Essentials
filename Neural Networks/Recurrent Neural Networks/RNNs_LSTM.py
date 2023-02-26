import tensorflow as tf
from tensorflow.keras import layers

# Define the LSTM model
model = tf.keras.Sequential()

# Add an LSTM layer with 64 units and input shape of (timesteps, input_dim)
model.add(layers.LSTM(64, input_shape=(10, 32)))

# Add a fully connected output layer with 1 neuron
model.add(layers.Dense(1, activation='sigmoid'))

# Compile the model with binary crossentropy loss and Adam optimizer
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model on a synthetic dataset
import numpy as np

# Generate some random data
data = np.random.randn(1000, 10, 32)
labels = np.random.randint(2, size=(1000, 1))

# Split the data into training and validation sets
x_train, y_train = data[:800], labels[:800]
x_val, y_val = data[800:], labels[800:]

# Train the model
model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=10, batch_size=32)
