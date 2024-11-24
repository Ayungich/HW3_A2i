import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных для стандартного MERGE SORT
merge_sort_data = pd.read_csv('merge_sort_timings.csv')

# Чтение данных для гибридного MERGE+INSERTION SORT
hybrid_sort_data = pd.read_csv('hybrid_merge_insertion_sort_timings.csv')

# Функция для построения графиков для одного типа данных
def plot_timings(data, sort_type, data_type):
    plt.figure(figsize=(10, 6))
    if sort_type == 'Standard Merge Sort':
        plt.plot(data['Size'], data[data_type], label=sort_type, marker='o')
    elif sort_type == 'Hybrid Merge+Insertion Sort':
        for threshold in data['Threshold'].unique():
            subset = data[data['Threshold'] == threshold]
            plt.plot(subset['Size'], subset[data_type], label=f'Threshold {threshold}', marker='o')
    plt.title(f'{sort_type} - {data_type} Array')
    plt.xlabel('Array Size')
    plt.ylabel('Average Time (ms)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{sort_type}_{data_type}.png')
    plt.show()

# Построение графиков для стандартного MERGE SORT
plot_timings(merge_sort_data, 'Standard Merge Sort', 'Random')
plot_timings(merge_sort_data, 'Standard Merge Sort', 'ReverseSorted')
plot_timings(merge_sort_data, 'Standard Merge Sort', 'NearlySorted')

# Построение графиков для гибридного MERGE+INSERTION SORT
plot_timings(hybrid_sort_data, 'Hybrid Merge+Insertion Sort', 'Random')
plot_timings(hybrid_sort_data, 'Hybrid Merge+Insertion Sort', 'ReverseSorted')
plot_timings(hybrid_sort_data, 'Hybrid Merge+Insertion Sort', 'NearlySorted')
