import pandas as pd

# Загрузка данных из файла CSV
name = 'radial'
data_path = '/Users/aboba/Desktop/isp/' + name + '.csv'  # Путь к исходному файлу данных
data = pd.read_csv(data_path, header=None)  # Считывание данных без заголовков столбцов

# Определение начальных координат и шага
start_x = -3.00  # Начальная координата X для самой нижней строки
start_y = 1.00   # Начальная координата Y для самого левого столбца
step = 1.00      # Шаг изменения координат

# Получение размеров таблицы
rows, cols = data.shape

# Определение пути для сохранения файла с результатами
output_path = '/Users/aboba/Desktop/isp/' + name + '.dat'  # Файл будет сохранен в доступной для загрузки директории

# Открытие файла для записи результатов
with open(output_path, 'w') as file:
    # Итерация по всем ячейкам датафрейма
    for row in range(rows):
        for col in range(cols):
            # Вычисление координат для текущей ячейки
            x = start_x + row * step  # Движемся вверх по строкам
            y = start_y + col * step  # Движемся вправо по столбцам
            value = data.iloc[row, col]  # Значение текущей ячейки
            # Запись координат и значения в файл
            file.write(f"{x:.2f} {y:.2f} {value}\n")
