from numpy import random as r
import time

import random

#Step1 choose 3 sorting algorithms quicksort mergesort insertionsort

#Step2 implement sorting algorithms
"""
#quicksort implementation
def partition(array, first, last):
    #choose last element as pivot
    pivot = array[last]
    
    #big pointer
    p= first-1
    
    #iterate through the array comparing with the pivot
    for i in range(first,last):
        if array[i]<=pivot:
            p = p + 1
            
            #swap element
            (array[p],array[i])=(array[i],array[p])
    #swap pivot with greater element
    (array[p+1],array[last])=(array[last],array[p+1])
    return p+1
    
def quicksort(array, low, high):
    if low<high:
        pi = partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
"""

# Python implementation QuickSort using 
# Lomuto's partition Scheme.

'''
The function which implements QuickSort.
arr :- array to be sorted.
start :- starting index of the array.
stop :- ending index of the array.
'''
def quicksort(arr, start , stop):
	if(start < stop):
		
		# pivotindex is the index where 
		# the pivot lies in the array
		pivotindex = partitionrand(arr,\
							start, stop)
		
		# At this stage the array is 
		# partially sorted around the pivot. 
		# Separately sorting the 
		# left half of the array and the
		# right half of the array.
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)

# This function generates random pivot,
# swaps the first element with the pivot 
# and calls the partition function.
def partitionrand(arr , start, stop):

	# Generating a random number between the 
	# starting index of the array and the
	# ending index of the array.
	randpivot = random.randrange(start, stop)

	# Swapping the starting element of
	# the array and the pivot
	arr[start], arr[randpivot] = \
		arr[randpivot], arr[start]
	return partition(arr, start, stop)

'''
This function takes the first element as pivot, 
places the pivot element at the correct position 
in the sorted array. All the elements are re-arranged 
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''
def partition(arr,start,stop):
	pivot = start # pivot
	
	# a variable to memorize where the 
	i = start + 1
	
	# partition in the array starts from.
	for j in range(start + 1, stop + 1):
		
		# if the current element is smaller
		# or equal to pivot, shift it to the
		# left side of the partition.
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] =\
			arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

# Driver Code
if __name__ == "__main__":
	array = [10, 7, 8, 9, 1, 5]
	quicksort(array, 0, len(array) - 1)
	print(array)

# This code is contributed by soumyasaurav

#mergesort implementation
#https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
#insertionsort implementation
def insertionSort(arr,n):
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

arraySizes = [10,100,1000]
quickSortRunTime = []
mergeSortRunTime = []
insertionSortRunTime = []
pythonDefaultSort =[]
for i in arraySizes:
    #Step3 Generate random Data
    array=r.randint(100000,size = i)
    copyarray = array.copy()
    copyarray2 = array.copy()
    copyarray3 = array.copy()
    
    #Step4 Measure Execution time
    start = time.time()
    quicksort(array,0,i-1)
    end = time.time()
    quickSortRunTime.append(end-start)
    
    start = time.time()
    mergeSort(copyarray,0,i-1)
    end = time.time()
    mergeSortRunTime.append(end-start)
    
    start = time.time()
    insertionSort(copyarray2,i)
    end = time.time()
    insertionSortRunTime.append(end-start)
    
    start = time.time()
    copyarray3.sort()
    end = time.time()
    pythonDefaultSort.append(end-start)
    

print(quickSortRunTime)
print(mergeSortRunTime)
print(insertionSortRunTime)
print(pythonDefaultSort)


#Step5 analyze time complexity
"""
Time complexity of quicksort
Average nlogn
Worst n^2
"""
#Step6 Visualize the Data
#maybe run a loop and calculate average time for each size and algorithm
