import pandas as pd

# Загрузка данных
file_path = '2_курс,1_сем_2020_21_уч_г_зима_от_27_01_2022_долги_все_институты.xlsx'
data = pd.read_excel(file_path)

# Очистка данных
data_cleaned = data.drop(columns=['№ \nп/п', 'ФИО', 'Номер ЛД'])

# Заполнение пропусков
data_cleaned = data_cleaned.fillna('Нет данных')

# Преобразование оценок в числовой формат
grade_mapping = {
    'Зач': 1, 'зачтено': 1, 'зачтена': 1, 'Экз': 1,
    'отлично': 5, 'хорошо': 4, 'удовлетворительно': 3,
    'неудовлетворительно': 2, 'неуд': 2, 'Неудовлетворительно': 2, 'Неуд': 2,
    'Отлично': 5, 'Хорошо': 4, 'Удовлетворительно': 3,
    'Неявка': 0, 'З/О': 1, 'Нет данных': 0
}

# Применение маппинга к оценкам
for col in data_cleaned.columns[4:-2]:
    data_cleaned[col] = data_cleaned[col].apply(lambda x: grade_mapping.get(str(x), 0))

# Преобразование 'Статус' в бинарный признак
data_cleaned['Статус'] = data_cleaned['Статус'].apply(lambda x: 1 if x == 'Отчислен' else 0)

# Замена 'Нет данных' на 0
data_cleaned.replace('Нет данных', 0, inplace=True)

# One-hot encoding для категориальных признаков
categorical_features = ['Институт', 'Учебная группа']
data_encoded = pd.get_dummies(data_cleaned, columns=categorical_features, drop_first=True)

# Сохранение подготовленных данных в новый файл
data_encoded.to_csv('prepared_student_data.csv', index=False)

# Вывод первых строк подготовленных данных
print(data_encoded.head())
