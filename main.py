import random
import timeit
import csv
import matplotlib.pyplot as plt

#CS404 MINI Project
#Name: David Lee


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def timsort(arr):
    return sorted(arr)

def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr


arraySizes = [10,100,1000,10000]
quickSortRunTime = []
mergeSortRunTime = []
bubbleSortRunTime = []
insertionSortRunTime = []
selectionSortRunTime = []
python_timSort =[]
countingSortRunTime = []
radixSortRunTime = []


# Function to measure execution time of a sorting algorithm
def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr)
    end_time = timeit.default_timer()
    return end_time - start_time

# Measure execution time for each sorting algorithm
for i in arraySizes:
    array = random.sample(range(100000), i)
    copyarray = array.copy()
    copyarray2 = array.copy()
    copyarray3 = array.copy()
    copyarray4 = array.copy()
    copyarray5 = array.copy()
    copyarray6 = array.copy()
    copyarray7 = array.copy()

    quickSortRunTime.append(measure_time(quicksort, array))
    mergeSortRunTime.append(measure_time(merge_sort, copyarray))
    bubbleSortRunTime.append(measure_time(bubble_sort, copyarray2))
    insertionSortRunTime.append(measure_time(insertion_sort, copyarray3))
    selectionSortRunTime.append(measure_time(selection_sort, copyarray4))
    python_timSort.append(measure_time(timsort, copyarray5))
    countingSortRunTime.append(measure_time(counting_sort, copyarray6))
    radixSortRunTime.append(measure_time(radix_sort, copyarray7))

# Generate the chart
plt.plot(arraySizes, quickSortRunTime, label='Quick Sort')
plt.plot(arraySizes, mergeSortRunTime, label='Merge Sort')
plt.plot(arraySizes, bubbleSortRunTime, label='Bubble Sort')
plt.plot(arraySizes, insertionSortRunTime, label='Insertion Sort')
plt.plot(arraySizes, selectionSortRunTime, label='Selection Sort')
plt.plot(arraySizes, python_timSort, label='Python TimSort')
plt.plot(arraySizes, countingSortRunTime, label='Counting Sort')
plt.plot(arraySizes, radixSortRunTime, label='Radix Sort')

# Add labels and title
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Sorting Algorithms')
# Add labels and title
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Sorting Algorithms')

# Change y axis to log scale
plt.yscale('log')
plt.xscale('log')
# Add legend
plt.legend()

# Show the chart
plt.show()

# Export arrays to CSV file
with open('sorting_runtimes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Array Size', 'Quick Sort', 'Merge Sort', 'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Python TimSort', 'Counting Sort', 'Radix Sort'])
    for i in range(len(arraySizes)):
        writer.writerow([arraySizes[i], quickSortRunTime[i], mergeSortRunTime[i], bubbleSortRunTime[i], insertionSortRunTime[i], selectionSortRunTime[i], python_timSort[i], countingSortRunTime[i], radixSortRunTime[i]])

