import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, mean_absolute_error
import joblib
import numpy as np
import lightgbm as lgb


# Загрузка данных
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')

# Создание модели

model = lgb.LGBMClassifier(
    learning_rate=0.01,
    max_depth=7,
    n_estimators=200,
    num_leaves=50,
    verbose=-1
)

# Обучение модели
model.fit(X_train, y_train)

# Сохранение модели
joblib.dump(model, 'model.pkl')

# Предсказание
y_pred = model.predict(X_test)



y_true = y_test['Доля 2 последний семестр'].values
accuracy = accuracy_score(y_true, y_pred)

# Оценка модели
mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

# Сохранение предсказаний
predictions_df = pd.DataFrame(y_pred, columns=['Predicted'])
predictions_df.to_csv('predictions.csv', index=False)


print(f"MAE: {mae:.2f}")

print(f"R^2 Score: {r2:.2f}")

print(f"Accuracy : {accuracy:.2f}")
