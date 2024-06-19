import tensorflow as tf
import pandas as pd

# Load preprocessed data (this assumes 'preprocessed_data.csv' is already created)
preprocessed_data = pd.read_csv('data/preprocessed_data.csv')
x_train = preprocessed_data.drop(columns=['failure'])
y_train = preprocessed_data['failure']

# Define a simple TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10)

# Save the trained model
model.save('models/trained_model.h5')
