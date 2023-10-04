import time
import numpy

def bubbleSort(A) :
    l = len(A)
    last = l-1
    sorted = False
    while(not sorted) :
        sorted = True  # assume sorted until we have to swap
        for index in range(last):
            if A[index] > A[index+1] :
                tmp = A[index]
                A[index] = A[index+1]
                A[index+1] = tmp
                sorted = False
        last = last -1 # A small optomisation


# MergeSort in Python
# Source https://www.geeksforgeeks.org/merge-sort/
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

# sort the items in data between index low and index high
def quickSort(data,low,high):
    # don't sort if single element
    if high <= low+1:
        return

    # find the mid point
    pivotPos = int((low+high) / 2)
    pivotVal = data[pivotPos]

    # split data into those less than the pivot
    lowvals =[]
    highvals =[]

    for i in range(low,high):
        if i == pivotPos:
            continue
        if data[i] < pivotVal:
            lowvals.append(data[i])
        else:
            highvals.append(data[i])

    # now assemble the sorted data
    index = low
    for val in lowvals:
        data[index] = val
        index+=1
    data[index] = pivotVal
    pivotPos = index
    index+=1
    for val in highvals:
        data[index] = val
        index+=1

    quickSort(data,low,pivotPos)
    quickSort(data,pivotPos+1,high)

# sort the items in data inplace 
# between index low and index high
def inPlaceQuickSort(data,low,high):
    # print("sorting between",low,high)
    # don't sort if single element
    if low >= high:
        return

    # find the mid point
    pivotPos = int((low+high) / 2)
    pivotVal = data[pivotPos]

    i = low
    j = high

    while True:
        # find index of first value on left > pivot
        while data[i] < pivotVal:
            i += 1
        # find index of first value on right < pivot
        while data[j] > pivotVal:
            j -= 1
        # if no element to be swapped, exit loop
        if i >= j:
            break
        # swap the items
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1

    # now sort the sublists
    inPlaceQuickSort(data,low,j)
    inPlaceQuickSort(data,j+1,high)


# function to test sorting
def sorting_test(alg_no,orig):
    data = numpy.array(orig).tolist() 

    t0 = time.perf_counter() # get time before sorting

    if alg_no == 1:
        bubbleSort(data)
    elif alg_no == 2:
        inPlaceQuickSort(data,0,len(data)-1)
    elif alg_no == 3:
        mergeSort(data) # merge sort algorithm in code
    elif alg_no == 4:
        data.sort()   # standard sort provided by pythons
    # data = numpy.sort(orig, kind='mergesort') # mergesort algorithm
    # data = numpy.sort(orig, kind='quicksort') # quicksort algorithm
    # data = numpy.sort(orig, kind='heapsort')  # heapsort algorithm
    # data = numpy.sort(orig, kind='stable')    # stable 

    t1 = time.perf_counter()
    diff = t1 - t0
    print("Size ",len(data),"time taken ", f'{diff:6f}')

    orig.sort()
    if not (data == orig).all():
        print("Not correctly sorted")


# Now lets see how long its takes to sort arrays of different sizes

data = [21,24,42,29,23,13,8,39,38]
print("sorting",data)
inPlaceQuickSort(data,0,len(data)-1)
print("sorted",data)

data = [37,20,17,26,44,41,27,28,50,17]
print("sorting",data)
inPlaceQuickSort(data,0,len(data)-1)
print("sorted",data)


#exit(0)

num_eles = 1
for size in range(15):
    num_eles = num_eles * 2             # double size each time
    data = numpy.random.rand(num_eles)  # generate a random array
    sorting_test(data)                  # run the test


