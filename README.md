# Time Complexity Analysis of Sorting Algorithms

## Overview
This repository contains code for analyzing the time complexity of sorting algorithms, specifically focusing on QuickSort, MergeSort, HeapSort, InsertionSort, and HybridSort. The analysis involves running experiments under various scenarios and list sizes to compare the runtime performance of these algorithms.

## Algorithms Included
- **QuickSort**: An efficient divide-and-conquer algorithm that sorts an array by partitioning it into smaller subarrays.
- **MergeSort**: Another divide-and-conquer algorithm that recursively divides the array into halves, sorts them, and then merges them back together.

## Experimental Setup
- All code provided is intended to be executed through an interactive environment. 
- Python is used as the primary programming language.
- Libraries such as matplotlib and numpy are utilized for data visualization and numerical operations.
- The runtime of each algorithm is measured using the time module in Python.

## List Generation Scenarios
The experiments consider the following scenarios for generating lists:
1. **Random**: Lists containing random integers within a specified range.
2. **Sorted**: Lists already sorted in ascending order.
3. **Reverse Sorted**: Lists sorted in descending order.
4. **Partially Sorted**: Lists mostly sorted with a few elements swapped randomly.

## Experimentation and Analysis
- The repository includes code to conduct experiments for different scenarios and list sizes.
- Each scenario is tested across multiple trials to ensure robustness of results.
- The runtime of each trial is recorded and analyzed to draw comparisons between QuickSort and MergeSort.

## Time Complexity
- QuickSort typically has an average time complexity of O(n log n), with worst-case time complexity of O(n^2) when the pivot selection is poor.
- MergeSort, on the other hand, maintains a consistent O(n log n) time complexity regardless of the input data, making it more predictable but potentially slower in some cases.

## Interactive Execution
To run the provided code and analyze the time complexity of sorting algorithms:
1. Ensure you have a Python environment set up.
2. Execute the code in an interactive environment such as Jupyter Notebook or any Python IDE.
3. Follow the provided instructions within the code comments to conduct experiments for different scenarios and list sizes.
