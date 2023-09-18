import tkinter as tk
import random
import time


# Create a class for the Sorting Visualizer application
class SortingVisualizer:
    def __init__(self, window):
        # Initialize the main window
        self.window = window
        self.window.title("Sorting Algorithm Visualizer")
        self.window.geometry("1040x680")  # Set the window size
        self.stop = False

        # Set up the canvas for visualization
        self.canvas_width, self.canvas_height = 1000, 450  # Set the canvas size
        self.canvas = tk.Canvas(
            self.window, width=self.canvas_width, height=self.canvas_height
        )
        self.canvas.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=20,
            pady=20,
            sticky="nsew",
        )  # Place canvas at the top, spanning all columns

        # Variables for algorithm selection and list size
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Bubble Sort")  # Default selection

        self.list_size_var = tk.IntVar()
        self.list_size_var.set(30)  # Default list size

        self.arr = []  # Store the current array

        # Create the user interface elements
        self.create_interface()

    def create_interface(self):
        # Left side (list size slider, and speed slider)
        left_frame = tk.Frame(self.window)
        left_frame.grid(row=1, column=0)

        # Label for list size slider
        list_size_label = tk.Label(left_frame, text="List Size:")
        list_size_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

        # Slider for adjusting list size
        list_size_slider = tk.Scale(
            left_frame,
            from_=10,
            to=100,
            orient="horizontal",
            length=200,
            variable=self.list_size_var,
        )
        list_size_slider.grid(row=1, column=0, columnspan=2)

        # Label for sorting speed slider
        speed_slider_label = tk.Label(left_frame, text="Sorting Speed:")
        speed_slider_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # Slider for adjusting sorting speed
        self.speed_slider = tk.Scale(
            left_frame, from_=1, to=100, orient="horizontal", length=200
        )
        self.speed_slider.set(50)  # Default speed
        self.speed_slider.grid(row=3, column=0, columnspan=2)

        # Right side (buttons and algorithm selection)
        right_frame = tk.Frame(self.window)
        right_frame.grid(row=1, column=1, padx=20)

        algorithms = ["Bubble Sort", "Selection Sort", "Quicksort", "Merge Sort"]

        label_frame = tk.Frame(right_frame)
        label_frame.grid(row=0, column=0, columnspan=3, pady=(0, 5), padx=(0, 100))

        # Label for algorithm selection
        algorithm_selection_label = tk.Label(
            label_frame, text="Select Sorting Algorithm:"
        )
        algorithm_selection_label.pack()

        # Radio buttons for selecting sorting algorithm
        for i, algorithm in enumerate(algorithms):
            algorithm_button = tk.Radiobutton(
                right_frame,
                text=algorithm,
                variable=self.algorithm_var,
                value=algorithm,
            )
            if i % 2 == 0:
                algorithm_button.grid(row=(i // 2) + 1, column=0, sticky="w")
            else:
                algorithm_button.grid(row=(i // 2) + 1, column=1, sticky="w")

        button_frame = tk.Frame(right_frame)
        button_frame.grid(
            row=(len(algorithms) // 2) + 1, column=0, columnspan=3, pady=(10, 0)
        )

        # Button to start sorting
        start_button = tk.Button(
            button_frame, text="Start Sorting", command=self.start_sorting
        )
        start_button.grid(row=0, column=0, padx=(0, 10))

        # Button to stop sorting
        stop_button = tk.Button(
            button_frame, text="Stop Sorting", command=self.stop_sorting
        )
        stop_button.grid(row=0, column=1, padx=(0, 10))

        # Button to generate a random array
        reset_button = tk.Button(
            button_frame,
            text="Generate Random Array",
            command=self.generate_random_array,
        )
        reset_button.grid(row=0, column=2)

    def update_list_size(self):
        # Update the array size based on the slider value
        size = self.list_size_var.get()
        self.arr = [random.randint(10, 450) for _ in range(size)]

    def start_sorting(self):
        # Start the selected sorting algorithm based on user input
        self.stop = False
        sorting_speed = int(self.speed_slider.get())
        selected_algorithm = self.algorithm_var.get()
        self.update_list_size()

        if selected_algorithm == "Bubble Sort":
            self.bubble_sort(self.arr, sorting_speed)
        elif selected_algorithm == "Selection Sort":
            self.selection_sort(self.arr, sorting_speed)
        elif selected_algorithm == "Merge Sort":
            self.merge_sort(self.arr, 0, len(self.arr) - 1, sorting_speed)
        elif selected_algorithm == "Quicksort":
            self.quick_sort(self.arr, 0, len(self.arr) - 1, sorting_speed)

    def generate_random_array(self):
        # Generate a new random array based on the slider value
        self.update_list_size()
        self.draw_bars(self.arr, -1, -1, 0.0001)

    def stop_sorting(self):
        # Stop the sorting process
        self.stop = True

    # The bubble_sort function implements the Bubble Sort algorithm,
    # which repeatedly compares adjacent elements and swaps them if they are in the wrong order.
    def bubble_sort(self, arr, sorting_speed):
        # Implementation of the Bubble Sort algorithm with visualization
        n = len(arr)
        for i in range(n):
            swapped = False  # Initialize a flag to track if any swaps were made
            for j in range(0, n - i - 1):
                if self.stop:
                    return
                if arr[j] > arr[j + 1]:
                    # Swap elements if they are in the wrong order
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

                    self.draw_bars(arr, j, j + 1, sorting_speed)
            if not swapped:
                break

    # The selection_sort function implements the Selection Sort algorithm,
    # which repeatedly selects the minimum element from the unsorted part of the array and moves it to the beginning.
    def selection_sort(self, arr, sorting_speed):
        # Implementation of the Selection Sort algorithm with visualization
        n = len(arr)
        for i in range(n):
            min_index = i  # Assume the current index holds the minimum value
            for j in range(i + 1, n):
                if self.stop:
                    return
                if arr[j] < arr[min_index]:
                    min_index = j
            # Swap the current element with the minimum element found
            arr[i], arr[min_index] = arr[min_index], arr[i]
            self.draw_bars(arr, i, min_index, sorting_speed)

    # The _merge_sort function is a recursive implementation of the Merge Sort algorithm.
    # It divides the array into two halves, recursively sorts each half, and then merges them back together.
    # Note that it is implemented this way to allow stop functionality (to not pass in a new "self")
    def merge_sort(self, arr, left, right, sorting_speed):
        self._merge_sort(arr, left, right, sorting_speed)

    def _merge_sort(self, arr, left, right, sorting_speed):
        if left >= right or self.stop:
            return

        mid = (left + right) // 2

        # Visualize the left and right subarrays before merging
        self.draw_bars(arr, left, mid, sorting_speed)

        self._merge_sort(arr, left, mid, sorting_speed)

        if self.stop:
            return

        self._merge_sort(arr, mid + 1, right, sorting_speed)

        if self.stop:
            return

        # Merge the subarrays
        self.merge(arr, left, mid, right)

        # Visualize the merged subarray
        self.draw_bars(arr, left, right, sorting_speed)

    # The merge function takes a list (arr) and merges two subarrays (left_half and right_half)
    # into a single sorted array. It uses pointers (i, j, and k) to iterate through the subarrays
    # and merge their elements into the main array in sorted order.
    def merge(self, arr, left, mid, right):
        # Merging two subarrays into a single sorted array

        # Extract the left and right subarrays from the main array
        left_half = arr[left : mid + 1]
        right_half = arr[mid + 1 : right + 1]

        i = j = 0  # Initialize pointers for the left and right subarrays
        k = left  # Initialize a pointer for the merged array

        # Compare elements from the left and right subarrays and merge them into the main array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Handle remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    # The quick_sort function is the main Quick Sort algorithm. It selects a pivot,
    # partitions the array into two subarrays, and recursively sorts them.
    def quick_sort(self, arr, low, high, sorting_speed):
        if low < high:
            # Find the pivot element and its final position (partitioning)
            pivot_index = self.partition(arr, low, high, sorting_speed)

            # Recursively sort elements before and after the pivot
            if self.stop:
                return
            self.quick_sort(arr, low, pivot_index - 1, sorting_speed)
            self.quick_sort(arr, pivot_index + 1, high, sorting_speed)

    def partition(self, arr, low, high, sorting_speed):
        # Helper function to partition the array and return the pivot's final position

        # Choose the rightmost element as the pivot
        pivot = arr[high]
        i = low - 1  # Initialize the index of the smaller element

        for j in range(low, high):
            if self.stop:
                return

            if arr[j] <= pivot:
                # Swap arr[i] and arr[j]
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                # Visualize the swap operation
                self.draw_bars(arr, i, j, sorting_speed)

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        # Visualize the final position of the pivot
        self.draw_bars(arr, i + 1, high, sorting_speed)

        return i + 1

    def draw_bars(self, arr, idx1, idx2, sorting_speed):
        # Visualize the current state of the array as bars on the canvas
        self.canvas.delete("all")
        bar_width = self.canvas_width // len(arr)
        for i in range(len(arr)):
            color = "blue" if i == idx1 or i == idx2 else "#C1CDCD"
            self.canvas.create_rectangle(
                i * bar_width,
                self.canvas_height,
                (i + 1) * bar_width,
                self.canvas_height - arr[i],
                fill=color,
            )
        self.window.update()
        time.sleep(
            0.5 - (sorting_speed - 1) * 0.005
        )  # Sleeps for a time inversely proportional to sorting speed


def main():
    # Create the main application window and run the tkinter main loop
    window = tk.Tk()
    app = SortingVisualizer(window)
    window.mainloop()


if __name__ == "__main__":
    main()
