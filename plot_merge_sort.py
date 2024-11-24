import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
data = pd.read_csv('merge_sort_timings.csv')

# Построение графиков
plt.figure(figsize=(12, 8))

# График для случайных массивов
plt.plot(data['Size'], data['Random'], label='Random Array', marker='o')

# График для обратных отсортированных массивов
plt.plot(data['Size'], data['ReverseSorted'], label='Reverse Sorted Array', marker='s')

# График для почти отсортированных массивов
plt.plot(data['Size'], data['NearlySorted'], label='Nearly Sorted Array', marker='^')

# Настройка графика
plt.title('Merge Sort Timing Analysis')
plt.xlabel('Array Size')
plt.ylabel('Average Time (ms)')
plt.legend()
plt.grid(True)

# Сохранение графика в файл
plt.savefig('merge_sort_timings.png')

# Отображение графика
plt.show()
