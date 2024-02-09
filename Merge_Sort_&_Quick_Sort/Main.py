# Import necessary libraries
import random          # Library for generating random numbers
import time            # Library for measuring time
import matplotlib.pyplot as plt  # Library for plotting graphs
import numpy as np     # Library for numerical operations
import math            # Library for mathematical functions

# Import custom sorting algorithms
from Merge_Sort import mergeSort  # Importing Merge Sort algorithm
from Quick_Sort import quickSort  # Importing Quick Sort algorithm

# Function to create a custom list
def create_custom_list(length, max_value, item=None, item_index=None):
    """
    Generates a custom list of random integers within a specified range and optionally inserts an item at a specific index.

    Parameters:
        length (int): The length of the list to be generated.
        max_value (int): The maximum value for randomly generated integers.
        item (int, optional): The item to be inserted into the list.
        item_index (int, optional): The index where the item is to be inserted.

    Returns:
        list: The generated custom list.
    """
    random_list = [random.randint(0,max_value) for i in range(length)]
    if item != None:
        random_list.insert(item_index, item)
    return random_list

# Function to run sorting algorithms and measure their runtime
def run_algorithms(function, array):
    """
    Runs a specified sorting algorithm on a given array and measures the runtime.

    Parameters:
        function (function): The sorting algorithm function to be executed.
        array (list): The array to be sorted.

    Returns:
        float: The runtime of the sorting algorithm in seconds.
    """
    start = time.time()

    if function == quickSort:
        function(array, 0, len(array) - 1)
    else:
        function(array)
    
    return time.time() - start

# Function to generate different types of lists
def create_list(size, scenario):
    """
    Generates a list based on a specified scenario.

    Parameters:
        size (int): The size of the list to be generated.
        scenario (str): The scenario defining the characteristics of the list.

    Returns:
        list: The generated list.
    """
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

# Function to conduct experiments for a given sorting algorithm, list size, and scenario
def experiment(function, size, trials, scenario):
    """
    Performs multiple trials of sorting algorithms on lists generated according to a specified scenario and measures the runtime for each trial.

    Parameters:
        function (function): The sorting algorithm function to be evaluated.
        size (int): The size of the list to be generated for each trial.
        trials (int): The number of trials to be conducted.
        scenario (str): The scenario defining the characteristics of the generated lists.

    Returns:
        list: A list containing the runtime of each trial.
    """
    temp = []
    for _ in range(trials):
        array = create_list(size, scenario)
        trial_time = run_algorithms(function, array.copy())
        temp.append(trial_time)
    return temp

# Function to draw and display the plot
def draw_show_plot(results, title):
    """
    Draws and displays a bar plot showing the runtime of sorting algorithms for different scenarios.

    Parameters:
        results (dict): A dictionary containing the runtime results for different sorting algorithms and scenarios.
        title (str): The title of the plot.
    """
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

# Define parameters
array_size = [200, 1000]  # Sizes of arrays for experimentation
trials = 20               # Number of trials for each scenario
sorting_algorithms = {'QuickSort': quickSort, 'MergeSort': mergeSort}  # Dictionary mapping algorithm names to functions
alg_results = {alg_name: {size: [] for size in array_size} for alg_name in sorting_algorithms}  # Nested dictionary to store results
scenarios = ['Random', 'Sorted', 'Reverse Sorted', 'Partially Sorted']  # Different scenarios for list generation

# Perform experiments for different scenarios, sorting algorithms, and list sizes
for size in array_size:
    for alg_name, function in sorting_algorithms.items():
        for scenario in scenarios:
            alg_results[alg_name][scenario] = experiment(function, size, trials, scenario)

# Draw and display plots for each scenario and list size
for size in array_size:
    for scenario in scenarios:
        results = {alg_name: alg_results[alg_name][scenario] for alg_name in sorting_algorithms}
        draw_show_plot(results, f"Sorting Algorithms - {scenario} - Array Size: {size}")
