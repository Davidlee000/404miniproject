from numpy import random
import time


#Step1 choose 3 sorting algorithms quicksort mergesort insertionsort

#Step2 implement sorting algorithms

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
    


arraySizes = [10,100,1000,10000,100000]
quicksortruntime =[]

for i in arraySizes:
    #Step3 Generate random Data
    array=random.randint(100000,size = i)
    start = time.time()
    #Step4 Measure Execution time
    quicksort(array,0,i-1)
    end = time.time()
    quicksortruntime.append(end-start)

print(quicksortruntime)
#Step5 analyze time complexity
"""
Time complexity of quicksort
Average nlogn
Worst n^2
"""
#Step6 Visualize the Data
#maybe run a loop and calculate average time for each size and algorithm
