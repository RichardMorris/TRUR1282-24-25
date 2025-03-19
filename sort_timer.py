import time
import random

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
        last = last -1 # A small optimisation


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

def fivelinequicksort(data):
    if(len(data)<1):
        return []
    pivotval = data[0]
    low = [x for x in data if x < pivotval]
    mid = [x for x in data if x == pivotval]
    high = [x for x in data if x > pivotval]
    qlow = fivelinequicksort(low)
    qhigh = fivelinequicksort(high)
    return qlow + mid + qhigh
    
# sort the items in data in-place 
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

class Node:
    def __init__(self): # sets up a Node with all variable none
        self.value = None
        self.left = None
        self.right = None

    def addItem(self,value):
        if self.value == None:  # if value not set for this node
            self.value = value  # use that value
        elif value < self.value:    # if the value is less than this node
                                    # add on left
            if self.left==None:     # if left node does not exist
                self.left = Node()  # make it
            self.left.addItem(value) # add item on the left
        else:
            if self.right==None:
                self.right=Node()
            self.right.addItem(value)

    def printTree(self):
        if self.left != None:
            self.left.printTree()
        print(self.value,end=', ')
        if self.right != None:
            self.right.printTree()
            
    def buildList(self,list):
        if self.left != None:
            self.left.buildList(list)
        list.append(self.value)
        if self.right != None:
            self.right.buildList(list)
        
        
def treeSort(data):

    rootNode = Node()   # The base of the tree

    for item in data:
        rootNode.addItem(item)
    res = []
    rootNode.buildList(res)
    return res
    

def merge(left, right):
    pl = 0
    pr = 0  
    res = []
    while pl < len(left) and pr < len(right):
        if left[pl] < right[pr]:
            res.append(left[pl])
            pl += 1
        else:
            res.append(right[pr])
            pr += 1
    while pl < len(left):
        res.append(left[pl])
        pl += 1
    while pr < len(right):  
        res.append(right[pr])
        pr += 1 
    return res

def updown_sort(arr):
    dir = 1
    last = arr.pop(0)
    res = [last]

    work = []
    for x in arr:
        if ( dir == 1 and x >= last ) or ( dir == -1 and x <= last ):
            work.append(x)
        else:

            if dir == -1:
                work.reverse()
            res = merge(res, work)
            work = [x]
            dir = - dir
        last = x
    res = merge(res, work)
    return res

# function to test sorting
def sorting_test(alg_no,orig):
    data=orig[:] # copy the original list
    t0 = time.perf_counter() # get time before sorting
    if alg_no == 1:
        bubbleSort(data)
    elif alg_no == 2:
        inPlaceQuickSort(data,0,len(data)-1)
    elif alg_no == 3:
        mergeSort(data) # merge sort algorithm in code
    elif alg_no == 4:
        data.sort()   # standard sort provided by pythons
    elif alg_no == 5:
        data = treeSort(orig)
    elif alg_no == 6:
        data = fivelinequicksort(orig)
    elif alg_no == 7:
        data = updown_sort(data)
    else:
        print("No algorithm selected")
    if len(data) <= 10:
        print("Original data",orig)
        print("Sorted data  ",data)
    else:
        print("Original data",orig[:10],"...")
        print("Data sorted",data[:10],"...")
        
    t1 = time.perf_counter()
    diff = t1 - t0
    print("Size ",len(data),"time taken ", f'{diff:6f}')

    orig.sort()
    if not (data == orig):
        print("Not correctly sorted")
        print(data)
        print(orig)


# Now lets see how long its takes to sort arrays of different sizes

print("Select the type of sort:")
print("  1 - bubble sort")
print("  2 - quick sort")
print("  3 - merge sort")
print("  4 - python's default sort")
print("  5 - tree sort")
print("  6 - five line quick sort")
print("  7 - up-down sort")
code = int(input("Enter code "))
while True:
    num_eles = int(input("Enter number of elements up to 10000, -1 to exit "))
    if num_eles == -1:
        break
    # generate a random array, uses Pythons List Comprehension syntax
    data = [random.randint(1,100000) for x in range(num_eles)]
    sorting_test(code,data)                  # run the test
