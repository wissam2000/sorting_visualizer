
# Sorting Algorithm Visualizer

The Sorting Algorithm Visualizer is a Python application built using the Tkinter library to visualize various sorting algorithms in action. It allows you to interactively explore how different sorting algorithms work and observe how they perform on different types of input data.

## Features

- **Visualization of sorting algorithms**: The application provides visualizations for the following sorting algorithms:

  - Bubble Sort
  - Selection Sort
  - Quicksort
  - Merge Sort

- **Adjustable parameters**: You can control the size of the input data and the sorting speed using sliders.

- **Interactive user interface**: The user interface includes radio buttons to select the sorting algorithm and buttons to start, stop, or reset the sorting process.

## Getting Started

To run the Sorting Algorithm Visualizer, you need to have Python and the Tkinter library installed on your computer.

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/sorting-visualizer.git
   ```

2. **Run the Application**:
    ```bash
    Copy code
    python sorting_visualizer.py
    ```

3. **Using the application**:

    <ol start="1">
    <li>Select a sorting algorithm from the available options.</li>
    <li>Adjust the list size and sorting speed sliders as desired.</li>
    <li>Click the "Start Sorting" button to visualize the sorting process.</li>
    <li>Use the "Stop Sorting" button to halt the sorting process if needed.</li>
    <li>Click "Generate Random Array" to create a new random input array.</li>
    </ol>


### Supported Sorting Algorithms

#### Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. It continues to do so until the entire array is sorted.

#### Selection Sort

Selection Sort divides the array into a sorted and an unsorted region. It repeatedly selects the minimum element from the unsorted region and moves it to the sorted region.

#### Quicksort

Quicksort uses a divide-and-conquer approach. It selects a pivot element and partitions the array into two subarrays: elements less than the pivot and elements greater than the pivot. It then recursively sorts the subarrays.

#### Merge Sort

Merge Sort divides the array into two halves, recursively sorts each half, and then merges them back together.
