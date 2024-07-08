import pandas as pd
import category_encoders as ce

import numpy as np
file_path = 'students_performance.csv'
data = pd.read_csv(file_path)

data.drop(0, inplace=True)
# Очистка данных
data_cleaned = data.drop(columns=['ФИО', 'Номер ЛД','Статус', 'index'] )

data_cleaned = data_cleaned.fillna('Нет данных')
grade_mapping = {
    'Зач': 1, 'зачтено': 1, 'зачтена': 1, 'Экз': 1,
    'отлично': 5, 'хорошо': 4, 'удовлетворительно': 3,
    'неудовлетворительно': 2, 'неуд': 2, 'Неудовлетворительно': 2, 'Неуд': 2,
    'Отлично': 5, 'Хорошо': 4, 'Удовлетворительно': 3,
    'Неявка': 0, 'З/О': 1, 'Нет данных': -1
}

for col in data_cleaned.columns[3:-1]:
    data_cleaned[col] = data_cleaned[col].apply(lambda x: grade_mapping.get(str(x), 0))





# Обрабатвыем колонку 'отчислен': 'да' - 1, 'нет' - 0
pd.set_option('future.no_silent_downcasting', True)
data_cleaned['result'] = data_cleaned['result'].replace({'да': 1, 'нет': 0})


# Проверяем результат

columns_to_encode = ['Институт', 'Учебная группа']

# Создаем объект CatBoost Encoder
catboost_encoder = ce.CatBoostEncoder(cols=columns_to_encode)

# Применяем CatBoost Encoding к данным
data_encoded = catboost_encoder.fit_transform(data_cleaned, data_cleaned['result'])

# Проверяем результат
data_encoded.head()

# Сохранение датафрейма в CSV файл
data_encoded.to_csv('prepared_data.csv', index=False)