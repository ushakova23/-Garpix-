import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
data_cleaned = pd.read_csv('prepared_dataset.csv')
target_column = 'Доля 2 последний семестр'
X = data_cleaned.drop(target_column,axis =1)
y = data_cleaned[target_column]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.22, random_state=52)
print("Размер тренировочного набора:", X_train.shape)
print("Размер тестового набора:", X_test.shape)
data_cleaned.to_csv('final_data.csv', index=False)
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)