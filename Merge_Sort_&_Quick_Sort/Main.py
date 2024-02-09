import random
import time
import timeit 
import matplotlib.pyplot as plt
import numpy as np
import math
from Merge_Sort import mergeSort
from Quick_Sort import quickSort

def create_custom_list(length, max_value, item=None, item_index=None):
    random_list = [random.randint(0,max_value) for i in range(length)]
    if item!= None:
        random_list.insert(item_index,item)
    return random_list

def run_algorithms(function, array):
    start = time.time()

    if function == quickSort:
        function(array, 0, len(array) - 1)
    else:
        function(array)
    
    return time.time() - start

def create_list(size, scenario):
    if scenario == 'Random':
        return create_custom_list(size, 1000000)
    elif scenario == 'Sorted':
        return list(range(size))
    elif scenario == 'Reverse Sorted':
        return list(range(size, 0, -1))
    elif scenario == 'Partially Sorted':
        sorted_list = list(range(1, size + 1))
        index1, index2 = random.sample(range(size), 2)
        sorted_list[index1], sorted_list[index2] = sorted_list[index2], sorted_list[index1]
        return sorted_list

    
def experiment(function, size, trials, scenario):
    temp = []
    for _ in range(trials):
        array = create_list(size, scenario)
        trial_time = run_algorithms(function, array.copy())
        temp.append(trial_time)
    return temp

def draw_show_plot(results, title):
    plt.figure(figsize=(16, 8))
    index = np.arange(len(results['QuickSort']))
    bar_width = 0.35

    quickSortGraph, color_1 = ('QuickSort', 'black')
    mergeSortGraph, color_2 = ('MergeSort', 'purple')

    plt.bar(index, results[quickSortGraph], bar_width, color=color_1, label=quickSortGraph)
    plt.bar(index + bar_width, results[mergeSortGraph], bar_width, color=color_2, label=mergeSortGraph)


    plt.xlabel('Test')
    plt.ylabel('Runtime (ms)')
    plt.yscale('log')
    plt.title(title)
    plt.xticks(index + 0.5 * bar_width, [f'Test {i + 1}' for i in range(len(results['QuickSort']))])
    plt.legend()
    plt.show()



array_size = [200, 1000]
trials = 20
sorting_algorithms = {'QuickSort': quickSort, 'MergeSort': mergeSort}
alg_results = {alg_name: {size: [] for size in array_size} for alg_name in sorting_algorithms}

scenarios = ['Random', 'Sorted', 'Reverse Sorted', 'Partially Sorted']


for size in array_size:
    for alg_name, function in sorting_algorithms.items():
        for scenario in scenarios:
            alg_results[alg_name][scenario] = experiment(function, size, trials, scenario)

for size in array_size:
    for scenario in scenarios:
        results = {alg_name: alg_results[alg_name][scenario] for alg_name in sorting_algorithms}
        draw_show_plot(results, f"Sorting Algorithms - {scenario} - Array Size: {size}")
