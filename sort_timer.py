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
        llen = len(L)
        mlen = len(M)
        while i < llen and j < mlen:
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < llen:
            array[k] = L[i]
            i += 1
            k += 1

        while j < mlen:
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
    

def mergeArrays(left, right):
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


class Merger:
    """Abstract base class for merging algorithms."""
    def merge(self, sequence):
        """Merge the sequence into the current state.
        
        Args:
            sequence: a sorted list to be merged in.
        """
        raise NotImplementedError
    
    def collapse(self):
        """Return the merged list and clear interal data."""
        raise NotImplementedError
    
class SimpleMerger(Merger):
    """Simple merger that uses a list to store the merged data."""
    def __init__(self):
        self.data = []
    
    def merge(self, sequence):
        self.data = mergeArrays(self.data, sequence)
        global max_queue_size
    
    def collapse(self):
        res = self.data
        self.data = []
        return res
    
class IncreasingLengthMerger(Merger):
    """The merger contains lists of increasing length
    say, [ [1], [2,3], [4,5,6,7,8]],
    Each item in the list is compare in turn, if its length is less than
    or equal the length of the input list, then the two lists are merge and the 
    result become the new input, tested against the next item in the list.
    For example if the input is [9] it is first compared with [1], their lengths
    are the same, so they are merged to form [1,9], 
    and the list [1] removed from the queue. 
    It is then compared with [2,3] again they are merged to form [1,2,3,9]. 
    In the next comparision the input is shorter, 
    so it is pushed to the from of the queue: [[1,2,3,9], [4,5,6,7,8]]. 
    This has better complexity, probably O(n log n). 
   """
    def __init__(self):
        self.queue = []
    
    def merge(self, sequence):
        while len(self.queue) > 0 and len(sequence) >= len(self.queue[0]):
            sequence = mergeArrays(self.queue.pop(0),sequence)
        self.queue.insert(0,sequence)
   
    def collapse(self):
        res = []
        for ele in self.queue: 
            res = mergeArrays(res,ele)
        self.queue.clear()
        return res

class DequeMerger(Merger):
    """A versions of the IncreasingLengthMerger that uses a deque.
    """
    def __init__(self):
        self.queue = deque()

    def merge(self, sequence):
        while len(self.queue) > 0 and len(sequence) >= len(self.queue[0]):
            sequence = mergeArrays(self.queue.popleft(),sequence)
        self.queue.appendleft(sequence)

    def collapse(self):
        res = []
        for ele in self.queue: 
            res = mergeArrays(res,ele)
        self.queue.clear()
        return res

class TreeMerger(Merger):
    """
    This merger mirrors the tree structure you find with merge sort.
    Conceptually it works as a binary tree built from the bottom up. 
    Elements are added at the bottom of a binary tree, the parent of each pair 
    contains the result of merging the two children. So the top of the 
    tree contains the sorted list. In practice we don't need the whole tree, 
    as soon as two child nodes are present the parent can be calculate 
    and the children removed. The partially compleated tree can be 
    represented as an array where the i-th element is the node at height i, measured from the bottom. 
    This can either be a sorted list or None, if its parent has been calculated.

    Consider repeatidly adding sequences [a],[b],[c],[d]. 
    The list is intially empty [], after adding [a] it is [[a]].
    After adding [b] it is [None,[a,b]], first [b] is merged with [a]
    the first element set to None, and the merged list [a,b]
    added at the end of the queue. Adding [c] sets the first element to None
    giving [[c],[ab]]. Adding [d] first merges it with [c], giving the list
    [cd], the first element is set to None and
    the second elements is tested. A second merge is performed and the result[abcd] 
    is added to end of the queue, giving a final queue of [None,None,[abcd]].
    """
    def __init__(self):
        self.queue = []

    def merge(self, sequence):
        index = 0
        for ele in self.queue:
            if ele == None:
                self.queue[index] = sequence
                return 
            sequence = mergeArrays(ele,sequence)
            self.queue[index] = None
            index += 1    
        self.queue.append(sequence)

    def collapse(self):
        res = []
        for ele in self.queue: 
            if ele != None:
                res = mergeArrays(res,ele)
        self.queue.clear()
        return res

def updown_sort(arr,merger):
    """Sort the array arr using the up-down sort algorithm and
    a given merging algorithm.
    Args:
        arr: The array to sort.
        merger: The merging algorithm to use.   """
    global max_queue_size
    dir = 1
    if len(arr) == 0:
        return arr
    last = arr[0]
    queue = []
    start = 0
    end = 0
    max_queue_size = 0
    for x in arr:
        if ( dir == 1 and x >= last ) or ( dir == -1 and x <= last ):
            pass
        else:
            if dir == -1:
                work = arr[end-1:start-1:-1]
            else:
                work = arr[start:end]
            merger.merge(work)
            start = end
            dir = - dir
        last = x
        end += 1

    if dir == -1:
        work = arr[end-1:start-1:-1]
    else:
        work = arr[start:end]
    merger.merge(work)

    res = merger.collapse()
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
            res = mergeArrays(res, work)
            work = [x]
            dir = - dir
        last = x
    if dir == -1:
        work.reverse()
    res = mergeArrays(res, work)
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

def dump(filename,original,actual=None,expected=None):
    with open(filename,"w") as f:
        f.write("Original data\n")
        f.write(str(original))
        if actual is not None:
            f.write("\nSorted data\n")
            f.write(str(actual))
        if expected is not None:
            f.write("\nPython sorted data\n")
            f.write(str(expected))

# function to test sorting
def sorting_test(alg_no,orig):
    data=orig[:] # copy the original list
    t0 = time.perf_counter() # get time before sorting
    if alg_no == '1':
        bubbleSort(data)
    elif alg_no == '2':
        inPlaceQuickSort(data,0,len(data)-1)
    elif alg_no == '3':
        mergeSort(data) # merge sort algorithm in code
    elif alg_no == '4':
        data.sort()   # standard sort provided by pythons
    elif alg_no == '5':
        data = treeSort(orig)
    elif alg_no == '6':
        data = fivelinequicksort(orig)
    elif alg_no == '7a':
        data = updown_sort(data,SimpleMerger())
    elif alg_no == '7b':
        data = updown_sort(data,IncreasingLengthMerger())
    elif alg_no == '7c':
        data = updown_sort(data,TreeMerger())
    elif alg_no == '7d':
        data = updown_sort(data,DequeMerger())
    elif alg_no == '8':
        data = cheat_sort(data)
    elif alg_no == 'd':
        dump("dump.txt",orig)
        sys.exit(0)
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
        dump("error.txt",orig,data,copy)
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
        alg_no = sys.argv[1]
        line = sys.argv[2]
        data = data_from_input(line)
        sorting_test(alg_no,data)
        sys.exit(0)
    if( len(sys.argv) == 4 ):
        alg_no = sys.argv[1]
        num_eles = int(sys.argv[2])
        data = read_file(sys.argv[3])
        sorting_test(alg_no,data)
        sys.exit(0)

    print("Select the type of sort:")
    print("  1 - bubble sort")
    print("  2 - quick sort")
    print("  3 - merge sort")
    print("  4 - python's default sort")
    print("  5 - tree sort")
    print("  6 - five line quick sort")
    print("  7a - up-down sort, simple merger")
    print("  7b - up-down sort, length queue merger")
    print("  7c - up-down sort, tree queue merger")
    print("  7d - up-down sort, deque merger")
    print("  8 - cheat sort")
    print("  d - dump the data to the data.txt file")
    code = input("Enter code ")
    while True:

        line  = input("Enter number of elements up to 10000, -1 to exit, p 10 50 for 10 sorted lists of 50 elements concatinated: ")
        if line == "-1":
            break
        data = data_from_input(line)
        sorting_test(code,data)                  # run the test
