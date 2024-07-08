import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Загрузка данных

X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')


# Преобразование столбцов, которые должны быть числовыми
X_train = X_train.apply(lambda x: x.str.replace(' ', '').astype(float) if x.dtype == 'object' else x)

X_test = X_test.apply(lambda x: x.str.replace(' ', '').astype(float) if x.dtype == 'object' else x)

# Создание модели дерева решений

model2 = LogisticRegression()
model2.fit(X_train, y_train)

y_pred = model2.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Точность:", accuracy)

