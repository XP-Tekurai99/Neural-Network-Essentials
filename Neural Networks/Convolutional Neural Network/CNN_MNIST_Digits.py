import tensorflow as tf
from tensorflow.keras import layers

# Define the CNN model
model = tf.keras.Sequential()

# Add a convolutional layer with 32 filters, a 3x3 kernel size, and ReLU activation
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

# Add a max pooling layer with a 2x2 pool size
model.add(layers.MaxPooling2D((2, 2)))

# Add another convolutional layer with 64 filters and a 3x3 kernel size
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Add another max pooling layer
model.add(layers.MaxPooling2D((2, 2)))

# Add a flattening layer to convert the output of the convolutional layers to a 1D vector
model.add(layers.Flatten())

# Add a fully connected layer with 128 neurons and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Add a dropout layer to help prevent overfitting
model.add(layers.Dropout(0.5))

# Add the output layer with 10 neurons (one for each class) and softmax activation
model.add(layers.Dense(10, activation='softmax'))

# Compile the model with categorical crossentropy loss and Adam optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model on MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Reshape the input data to (28, 28, 1) and normalize the pixel values
x_train = x_train.reshape((60000, 28, 28, 1))
x_train = x_train.astype('float32') / 255
x_test = x_test.reshape((10000, 28, 28, 1))
x_test = x_test.astype('float32') / 255

# Convert the labels to categorical format
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))
