# NumPy Tutorial - Notes and Examples

# Import NumPy
import numpy as np

# Example: Creating a NumPy array
arr = np.array([1, 2, 3, 4])  # 1D array
print(arr)

# Example: Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# Example: Using np.arange() to create an array
arr_range = np.arange(10)  # array from 0 to 9
print(arr_range)

# Example: Creating an array of ones
ones_arr = np.ones((3, 3))  # 3x3 array of ones
print(ones_arr)

# Example: Creating an array of zeros
zeros_arr = np.zeros((2, 4))  # 2x4 array of zeros
print(zeros_arr)

# --- NumPy Array Indexing ---
# Indexing in NumPy works similarly to Python lists, but it supports multi-dimensional arrays.
# Example: Accessing an element in a 1D array
element = arr[2]  # Access the 3rd element (index 2)
print(element)

# Example: Accessing an element in a 2D array
element_2d = arr_2d[1, 2]  # Access element at row 1, column 2
print(element_2d)

# --- NumPy Array Slicing ---
# Slicing works similarly to Python lists but can be applied to multi-dimensional arrays.

# Example: Slicing a 1D array
slice_1d = arr[1:3]  # Elements from index 1 to 2
print(slice_1d)

# Example: Slicing a 2D array
slice_2d = arr_2d[1, 1:]  # Slice from row 1, column 1 to the end
print(slice_2d)

# --- NumPy Data Types ---
# NumPy supports various data types. You can specify the type using the dtype argument.
arr_int = np.array([1, 2, 3], dtype=int)  # integer array
arr_float = np.array([1.1, 2.2, 3.3], dtype=float)  # float array


# --- NumPy Copy vs View ---
# By default, NumPy passes arrays by reference. You can make a copy using arr.copy(), otherwise, you'll be working with a view.
# Example: Copy vs View
arr_copy = arr.copy()  # Make a copy of the array
arr_view = arr.view()  # Create a view of the array

# Modifying arr_copy won't affect arr, but modifying arr_view will affect arr.
arr_copy[0] = 99
arr_view[0] = 88

print("Original Array:", arr)
print("Copy:", arr_copy)
print("View:", arr_view)

# --- NumPy Array Shape ---
# The shape of an array tells you how many elements it has along each axis.
print("Shape of 2D array:", arr_2d.shape)  # Output (2, 3)

# --- NumPy Array Reshape ---
# You can change the shape of an array using reshape(). This does not alter the original array but returns a new one.
arr_reshaped = arr_range.reshape(2, 5)  # Reshape to 2x5
print(arr_reshaped)

# --- NumPy Array Iterating ---
# You can iterate over NumPy arrays with loops, similar to Python lists.

# Example: Iterating over a 1D array
for x in arr:
    print(x)

# Example: Iterating over a 2D array
for row in arr_2d:
    print(row)

# --- NumPy Array Join ---
# You can join arrays using np.concatenate() or np.vstack(), np.hstack() for vertical/horizontal stacking.
arr_concat = np.concatenate([arr, arr])  # Concatenate two arrays
print("Concatenated array:", arr_concat)

# Example: Horizontal and vertical stacking
arr_stack_h = np.hstack([arr_2d, arr_2d])  # Horizontal stack
arr_stack_v = np.vstack([arr_2d, arr_2d])  # Vertical stack
print("Horizontal Stack:\n", arr_stack_h)
print("Vertical Stack:\n", arr_stack_v)

# --- NumPy Array Split ---
# You can split arrays into multiple sub-arrays using np.split().
arr_split = np.split(arr_range, 2)  # Split into 2 sub-arrays
print(arr_split)

# --- NumPy Array Search ---
# You can search for values in an array using conditions.

# Example: Find elements greater than 5
arr_search = arr_range[arr_range > 5]
print("Elements greater than 5:", arr_search)

# --- NumPy Array Sort ---
# You can sort arrays using np.sort(). This does not change the original array by default.
arr_sorted = np.sort(arr_range)
print("Sorted Array:", arr_sorted)

# Example: Sorting a 2D array along an axis
arr_2d_sorted = np.sort(arr_2d, axis=1)  # Sort each row individually
print("Sorted 2D Array:\n", arr_2d_sorted)

# --- NumPy Array Filter ---
# You can filter arrays based on conditions, returning elements that satisfy the condition.

# Example: Filter elements in array less than 3
arr_filter = arr[arr < 3]
print("Filtered Array (less than 3):", arr_filter)


