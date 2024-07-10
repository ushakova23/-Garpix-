import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib


# Загрузка данных

X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')


# Преобразование столбцов, которые должны быть числовыми
#X_train = X_train.apply(lambda x: x.str.replace(' ', '').astype(float) if x.dtype == 'object' else x)

#X_test = X_test.apply(lambda x: x.str.replace(' ', '').astype(float) if x.dtype == 'object' else x)

# Создание модели

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Сохранение модели
joblib.dump(model, 'model.pkl')

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
predictions_df = pd.DataFrame(y_pred, columns=['Predicted'])
predictions_df.to_csv('predictions.csv', index=False)

print("Точность:", accuracy)


