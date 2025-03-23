import time
import random
import sys
import ast
from collections import deque

MAXVAL = 100000

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
    """ merge two sorted arrays into a single sorted array """
    llen = len(left)
    rlen = len(right)
    # fastest way the initilise a list
    res = [0] * (llen+rlen) # result array of lenght llen+rlen
    index = 0 # index into the result array
    pl = 0 # index into the left array
    pr = 0 # index into the right array 
    while pl < llen and pr < rlen:
        if left[pl] < right[pr]:
            res[index] = left[pl]
            index += 1
            pl += 1
        else:
            res[index] = right[pr]
            index += 1  
            pr += 1
    while pl < llen:
        res[index] = left[pl]
        index += 1
        pl += 1
    while pr < rlen:  
        res[index] = right[pr]
        index += 1
        pr += 1 
    return res

def merge_queue(queue, list):
    """merger a list into a queue of lists
    The qeues cointains lists of increasing length: [ [1], [2,3], [4,5,6,7] ]
    if the incoming list [8,9] is added it is compared to each list in the queue
    if the incoming list is longer than the list in the queue it is merged with the list
    and the result is added to the queue
    """
    while len(queue) > 0 and len(list) >= len(queue[0]):
        list = merge(queue.pop(0),list)
    queue.insert(0,list)
    return queue

def merge_queue3(queue, list):
    """merger a list into a queue of lists
    A possibly more efficient version of merge_queue, 
    that aims to remove the O(n) operation pop(0) and insert(0, v).  
    Here the entries in the queue are either a list or None.
    When adding a list each element is tested in turn,
    if its None it is replaced with the list and the function returns. 
    If it is a list the element is replaced by Node
    and element is merged into the incoming list.
    If the end of the list is reached the incoming list is added to the queue.
    In effect this mimics the behaviour of merge sort, with pairs of
    elements megered in the first level, quartets in the second level etc.
    It can also be through of as a binary tree, with items added at the bottom of the 
    tree and the parent node containing the the result of merging
    the two children. 

    Consider repeatidly adding lists [a],[b],[c],[d].
    The queue is intially empty [], after adding [a] it is [a].
    After adding [b] it is [None,[ab]], first [b] is merged with [a]
    the first element set to None, and the merged list [a,b]
    added at the end of the queue. Adding [c] sets the first element to None
    giving [[c],[ab]]. Adding [d] first merges it with [c], giving the list
    [cd], the first element is set to None and
    the second elements is tested. A second merge is performed and the result
    [abcd] is added to end of the queue, giving a final queue of [None,None,[abcd]]
    """
    index = 0
    for ele in queue:
        if ele == None:
            queue[index] = list
            return queue
        list = merge(ele,list)
        queue[index] = None
        index += 1    
    queue.append(list)
    return queue

def collapse_queue(queue):
    """ meger all the lists in the queue into a single list """
    res = []
    for ele in queue: 
        res = merge(res,ele)
    queue.clear()
    return res

def collapse_queue3(queue):
    """ meger all the lists in the queue into a single list """
    res = []
    for ele in queue: 
        if ele != None:
            res = merge(res,ele)
    queue.clear()
    return res

def updown_sort(arr):
    dir = 1
    last = arr[0]
    queue = []
    start = 0
    end = 0
    for x in arr:
        if ( dir == 1 and x >= last ) or ( dir == -1 and x <= last ):
            pass
        else:
            if dir == -1:
                work = arr[end-1:start-1:-1]
            else:
                work = arr[start:end]
            merge_queue(queue,work)
            start = end
            dir = - dir
        last = x
        end += 1

    if dir == -1:
        work = arr[end-1:start-1:-1]
    else:
        work = arr[start:end]
    merge_queue(queue,work)

    res = collapse_queue(queue)
    return res

def updown_sort2(arr):
    dir = 1
    last = arr[0]
    queue = []
    start = 0
    end = 0
    for x in arr:
        if ( dir == 1 and x >= last ) or ( dir == -1 and x <= last ):
            pass
        else:
            if dir == -1:
                work = arr[end-1:start-1:-1]
            else:
                work = arr[start:end]
            merge_queue3(queue,work)
            start = end
            dir = - dir
        last = x
        end += 1

    if dir == -1:
        work = arr[end-1:start-1:-1]
    else:
        work = arr[start:end]
    merge_queue3(queue,work)

    res = collapse_queue3(queue)
    return res

def updown_sort_old(arr):
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
    if dir == -1:
        work.reverse()
    res = merge(res, work)
    return res

def cheat_sort(arr):
    counts = [0] * (MAXVAL+1)
    for x in arr:
        counts[x] += 1
    data = [0] * len(arr)
    index = 0
    for i in range(0,len(counts)):
        for j in range(0,counts[i]):
            data[index] = i
            index += 1
    return data

def insert(data, value):
    ldata = len(data)
    if ldata == 0:
        data.append(value)
        return
    if value <= data[0]:
        data.insert(0,value)
        return
    prev = data[0]
    for i in range(1,ldata):
        if value <= data[i]:
            data.insert(i,value)
            return
        prev = data[i]
    data.append(value)

    
def heep_sort(arr,nbins):
    bins = [ [] for x in range(nbins) ]
    size = MAXVAL / nbins
    for x in arr:
        pos = int(x / size)
        insert(bins[pos],x)
    res = []
    for b in bins:
        res += b
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
    elif alg_no == 8:
        data = updown_sort2(data)
    elif alg_no == 9:
        data = cheat_sort(data)
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

    copy = orig[:]
    copy.sort()
    if not (data == copy):
        print("Not correctly sorted")
        print("Original data",len(orig))
        print("Sorted data  ",len(data))
        with open("error.txt","w") as f:
            f.write("Original data\n")
            f.write(str(orig))
            f.write("\nSorted data\n")
            f.write(str(data))
            f.write("\nPython sorted data\n")
            f.write(str(copy))
        sys.exit(1)

def read_file(filename):
    data = []
    with open(filename) as f:
        line1 = f.readline()
        line2 = f.readline()
        list = ast.literal_eval(line2)
    return list

def partial_sorted(n,maxsize):
    res =[]
    for i in range(0,n):
        #size = random.randint(1,maxsize)
        data = [random.randint(1,100000) for x in range(maxsize)]
        data.sort()
        res += data
    return res

def data_from_input(line):
    if line.startswith("p"):
        part = line.split(' ')
        num_parts = int(part[1])
        maxsize = int(part[2])
        data = partial_sorted(num_parts,maxsize)
    else:
        num_eles = int(line)
        # generate a random array, uses Pythons List Comprehension syntax
        data = [random.randint(1,MAXVAL) for x in range(num_eles)]
    return data



if __name__ == '__main__':

    if(len(sys.argv) == 3):
        alg_no = int(sys.argv[1])
        line = sys.argv[2]
        data = data_from_input(line)
        sorting_test(alg_no,data)
        sys.exit(0)
    if( len(sys.argv) == 4 ):
        num_eles = int(sys.argv[1])
        num_eles = int(sys.argv[2])
        data = read_file(sys.argv[3])
        sorting_test(2,data)
        sys.exit(0)

    print("Select the type of sort:")
    print("  1 - bubble sort")
    print("  2 - quick sort")
    print("  3 - merge sort")
    print("  4 - python's default sort")
    print("  5 - tree sort")
    print("  6 - five line quick sort")
    print("  7 - up-down sort")
    print("  8 - up-down sort v2")
    print("  9 - cheat sort")
    code = int(input("Enter code "))
    while True:

        line  = input("Enter number of elements up to 10000, -1 to exit, p 10 50 for 10 sorted lists of 50 elements concatinated: ")
        if line == "-1":
            break
        data = data_from_input(line)
        sorting_test(code,data)                  # run the test
