import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Reshape
from tensorflow.keras.models import Sequential

# Define the generator network
def build_generator(input_size):
    model = Sequential()
    model.add(Dense(128, input_dim=input_size, activation='relu'))
    model.add(Dense(784, activation='sigmoid'))
    model.add(Reshape((28, 28, 1)))
    return model

# Define the discriminator network
def build_discriminator():
    model = Sequential()
    model.add(Flatten(input_shape=(28, 28, 1)))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model

# Define the GAN network
def build_gan(generator, discriminator):
    model = Sequential()
    model.add(generator)
    model.add(discriminator)
    return model

# Load the MNIST dataset
(x_train, _), (_, _) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32')
x_train = (x_train - 127.5) / 127.5

# Define the hyperparameters
latent_dim = 100
batch_size = 128
epochs = 10000

# Build the networks
generator = build_generator(latent_dim)
discriminator = build_discriminator()
gan = build_gan(generator, discriminator)

# Compile the discriminator network
discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Compile the GAN network
gan.compile(loss='binary_crossentropy', optimizer='adam')

# Train the GAN
for epoch in range(epochs):
    # Generate random noise as input for the generator network
    noise = np.random.normal(0, 1, size=(batch_size, latent_dim))
    
    # Generate fake images using the generator network
    generated_images = generator.predict(noise)
    
    # Combine the fake and real images into a single dataset
    real_images = x_train[np.random.randint(0, x_train.shape[0], size=batch_size)]
    x = np.concatenate([generated_images, real_images])
    
    # Assign labels to the fake and real images
    y_dis = np.zeros(2*batch_size)
    y_dis[:batch_size] = 0.9 # Label real images as 0.9 (not 1 to prevent discriminator from overfitting)
    
    # Train the discriminator network
    discriminator.trainable = True
    discriminator.train_on_batch(x, y_dis)
    
    # Train the generator network
    noise = np.random.normal(0, 1, size=(batch_size, latent_dim))
    y_gen = np.ones(batch_size)
    discriminator.trainable = False
    gan.train_on_batch(noise, y_gen)
    
    # Print the loss and accuracy every 100 epochs
    if epoch % 100 == 0:
        print("Epoch: {0}, Discriminator Loss: {1:.4f}, Discriminator Accuracy: {2:.2f}%, Generator Loss: {3:.4f}".format(epoch, discriminator.history.history['loss'][-1], 100*discriminator.history.history['accuracy'][-1], gan.history.history['loss'][-1]))
