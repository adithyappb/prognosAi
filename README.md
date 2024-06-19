## PrognosAI

# Overview

PrognosAI is an AI-driven predictive maintenance system using TensorFlow and MLOps practices. It predicts equipment failures with high accuracy, reducing maintenance costs and enhancing system performance.

# Directory Structure

- `data/`: Contains CSV files (`equipment_data.csv`, `failure_data.csv`, etc.) for equipment and failure data used in analysis.
- `models/`: Stores the trained TensorFlow model (`trained_model.h5`) and related evaluation scripts.
- `scripts/`: Includes Python scripts (`data_preprocessing.py`, `train_model.py`, etc.) for data preprocessing, model training, and other tasks.
- `config/`: Holds configuration files (`config.yaml`, `ha_proxy_config.conf`, `pivotal_gemfire_config.xml`) used for system configuration.
- `README.md`: This file providing an overview of the project, its components, and usage instructions.
- `requirements.txt`: Lists Python dependencies required to run the project.

# Usage

1. **Data Preparation**: Place relevant CSV files in the `data/` directory.
2. **Environment Setup**: Install dependencies using `pip install -r requirements.txt`.
3. **Data Preprocessing**: Run `python scripts/data_preprocessing.py` to preprocess data.
4. **Model Training**: Execute `python scripts/train_model.py` to train the TensorFlow model.
5. **Model Evaluation**: Open `models/model_evaluation.py` to evaluate the model.

# Results

- **Predictive Accuracy**: Achieved high accuracy in predicting equipment failures.
- **Cost Reduction**: Significant reduction in maintenance costs.
- **Performance Enhancement**: Improved system performance through MLOps practices.
