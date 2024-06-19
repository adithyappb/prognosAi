import pandas as pd
import tensorflow as tf

def evaluate_model(model_path, test_data_path):
    # Load the trained model
    model = tf.keras.models.load_model(model_path)

    # Load test data
    test_data = pd.read_csv(test_data_path)
    x_test = test_data[['feature1', 'feature2', 'feature3']]  # Adjust column names if necessary
    y_test = test_data['target_column']

    # Evaluate the model
    test_loss, test_acc = model.evaluate(x_test, y_test)

    print('Test accuracy:', test_acc)

if __name__ == '__main__':
    # Define paths
    model_path = 'models/trained_model.h5'
    test_data_path = 'data/test_data.csv'

    # Evaluate the model
    evaluate_model(model_path, test_data_path)

