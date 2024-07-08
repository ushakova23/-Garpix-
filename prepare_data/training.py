import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Загрузка данных

X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')

print(X_test)
# Преобразуйте все столбцы, которые должны быть числовыми
X_train = X_train.apply(lambda x: x.str.replace(' ', '').astype(float) if x.dtype == 'object' else x)
# Преобразуйте все столбцы, которые должны быть числовыми
X_test = X_test.apply(lambda x: x.str.replace(' ', '').astype(float) if x.dtype == 'object' else x)
print(X_test)
# Создание модели дерева решений
model = DecisionTreeClassifier()


# Обучение модели
model.fit(X_train, y_train)

# Делаем предсказания на тестовой выборке
predictions = model.predict(X_test)

# Оцениваем модель
accuracy = accuracy_score(y_test, predictions)
print("Точность модели:", accuracy)





model2 = LogisticRegression()
model2.fit(X_train, y_train)

y_pred = model2.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Точность:", accuracy)

