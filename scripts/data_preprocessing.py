import pandas as pd

def preprocess_data(equipment_data_path, failure_data_path, output_path):
    # Load equipment data and failure data
    equipment_data = pd.read_csv(equipment_data_path)
    failure_data = pd.read_csv(failure_data_path)

    # Merge equipment and failure data
    combined_data = pd.merge(equipment_data, failure_data, on='equipment_id')

    # Save the preprocessed data
    combined_data.to_csv(output_path, index=False)

if __name__ == "__main__":
    equipment_data_path = 'data/equipment_data.csv'
    failure_data_path = 'data/failure_data.csv'
    output_path = 'data/preprocessed_data.csv'
    preprocess_data(equipment_data_path, failure_data_path, output_path)

