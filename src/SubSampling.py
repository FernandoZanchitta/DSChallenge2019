"""
Esse arquivo contém a implementação do método de SubAmostragem dos dados.
Esses dados podem ser encontrados no url:

https://www.kaggle.com/competitions/data-science-challenge-at-eef-2019/data

Baixe os arquivos e coloque-os na pasta dataset.
entre na pasta src/ e execute o comando:
python3 SubSampling.py
Preencha os nomes dos arquivos baixados na variável FILE_NAMES.

O resultado será a criação de 3 arquivos:
features-training-subsampled.csv
features-test-subsampled.csv
target-training-subsampled.csv
"""

FILE_NAMES = ["features-training", "features-test", "target-training"]


import pandas as pd
import os.path  

# Define the desired subsampling ratio
subsampling_ratio = 0.02  # 1/10 of the rows

# Define the file path
file_path_feature_training = f'../dataset/{FILE_NAMES[0]}.csv'
file_path_feature_test = f'../dataset/{FILE_NAMES[1]}.csv'
file_path_target_training = f'../dataset/{FILE_NAMES[2]}.csv'


# if file does not exist:
if not os.path.exists('../dataset/features-training-subsampled.csv'):
    print("File features-training-subsampled.csv not found!")
    # Read the CSV file
    feature_training = pd.read_csv(file_path_feature_training)

    # Subsample the dataframe
    feature_training_subsampled = feature_training.sample(frac=subsampling_ratio, random_state=42)

    # Now `feature_training_subsampled` contains the subsampled data

    feature_training_subsampled.to_csv('../dataset/features-training-subsampled.csv', index=False)

if not os.path.exists('../dataset/features-test-subsampled.csv'):
    print("File features-test-subsampled.csv not found!")
    ### Feature Test

    # Read the CSV file
    feature_test = pd.read_csv(file_path_feature_test)

    # Subsample the dataframe
    feature_test_subsampled = feature_test.sample(frac=subsampling_ratio, random_state=42)

    # Now `feature_training_subsampled` contains the subsampled data

    feature_test_subsampled.to_csv('../dataset/features-test-subsampled.csv', index=False)

### Target Training
if not os.path.exists('../dataset/target-training-subsampled.csv'):
    print("File target-training-subsampled.csv not found!")
    # Read the CSV file
    target_training = pd.read_csv(file_path_target_training)

    # Subsample the dataframe
    target_training_subsampled = target_training.sample(frac=subsampling_ratio, random_state=42)

    # Now `feature_training_subsampled` contains the subsampled data

    target_training_subsampled.to_csv('../dataset/target-training-subsampled.csv', index=False)