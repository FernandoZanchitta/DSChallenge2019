"""
Esse arquivo contém a implementação do método de SubAmostragem dos dados.
Esses dados podem ser encontrados no url:

https://www.kaggle.com/competitions/data-science-challenge-at-eef-2019/data
"""
import pandas as pd

# Define the desired subsampling ratio
subsampling_ratio = 0.1  # 1/10 of the rows

# Define the file path
file_path_feature_training = '../dataset/features-training.csv'
file_path_feature_test = '../dataset/features-test.csv'
file_path_target_training = '../dataset/target-training.csv'


# Read the CSV file
feature_training = pd.read_csv(file_path_feature_training)

# Subsample the dataframe
feature_training_subsampled = feature_training.sample(frac=subsampling_ratio, random_state=42)

# Now `feature_training_subsampled` contains the subsampled data

feature_training_subsampled.to_csv('../dataset/feature-training-subsampled.csv', index=False)
### Feature Test

# Read the CSV file
feature_test = pd.read_csv(file_path_feature_test)

# Subsample the dataframe
feature_test_subsampled = feature_test.sample(frac=subsampling_ratio, random_state=42)

# Now `feature_training_subsampled` contains the subsampled data

feature_test_subsampled.to_csv('../dataset/feature-test-subsampled.csv', index=False)

### Target Training

# Read the CSV file
target_training = pd.read_csv(file_path_target_training)

# Subsample the dataframe
target_training_subsampled = target_training.sample(frac=subsampling_ratio, random_state=42)

# Now `feature_training_subsampled` contains the subsampled data

target_training_subsampled.to_csv('../dataset/target-training-subsampled.csv', index=False)