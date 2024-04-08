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
    


#Step3 Generate random Data
Array10=random.randint(10000,size =10)
Array100=random.randint(10000,size = 100)
Array1000=random.randint(10000,size = 1000)
Array10000=random.randint(10000,size =10000)


#Step4 Measure Execution time
start = time.time()
quicksort(Array10,0,9)
end = time.time()

print("Time for running quicksort with 10 elements")
print (end-start)

start = time.time()
quicksort(Array100,0,99)
end = time.time()

print("Time for running quicksort with 100 elements")
print (end-start)

start = time.time()
quicksort(Array1000,0,999)
end = time.time()

print("Time for running quicksort with 1000 elements")
print (end-start)

start = time.time()
quicksort(Array10000,0,9999)
end = time.time()

print("Time for running quicksort with 10000 elements")
print (end-start)

#Step5 analyze time complexity
"""
Time complexity of quicksort
Average nlogn
Worst n^2
"""
#Step6 Visualize the Data
#maybe run a loop and calculate average time for each size and algorithm
