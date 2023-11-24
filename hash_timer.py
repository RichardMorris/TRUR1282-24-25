import time
import random

class Pair:
    def __init__(self,key,value): # sets up a Node with all variable none
        self.key = key # build an array with size elements
        self.value = value
    
    
class HashTable:
    def __init__(self,size): # sets up a Node with all variable none
        self.buckets = [None] * size # build an array with size elements
        self.size = size
        
    def addKeyValue(self,key,value):
        keyVal = Pair(key,value)
        hashValue = hash(key)
        bucketNo = hashValue % self.size
        if self.buckets[bucketNo] == None:
            self.buckets[bucketNo] = []
        list = self.buckets[bucketNo]
        list.append(keyVal)
    
    def getValue(self,key):
        hashValue = hash(key)
        bucketNo = hashValue % self.size
        if self.buckets[bucketNo] == None:
            print("Key "+str(key)+" not found")
            return None
        list = self.buckets[bucketNo]
        for ele in list:
            if ele.key == key:
                return ele.value
        print("Key "+str(key)+" not found")
        return None
        
# function to test sorting1
def hash_test(n_eles,n_bin,n_lookup):
    table = HashTable(n_bin)
    for ele in range(n_eles):
        table.addKeyValue(ele, ele*ele)     # store the element as
    
    data = [random.randint(0,n_eles-1) for x in range(n_lookup)]

    
    t0 = time.perf_counter() # get time before sorting

    for key in data:
        val = table.getValue(key)
        if val != key*key:
            print("Error ",key,val)
        
    t1 = time.perf_counter()
    diff = t1 - t0
    avg = diff / n_lookup
    print("Size ",len(data),"time taken ", f'{diff:6f}'," average ",f'{avg:6f}')


# Now lets see how long its takes to sort arrays of different sizes

while True:
    num_bins = int(input("Enter number of bins in the table, -1 to exit, 1 is effectively a linear search "))
    if num_bins == -1:
        break
    num_eles = int(input("Enter number of elements to add to table"))
    num_lookups = int(input("Enter number of lookups in the table"))
    hash_test(num_eles, num_bins, num_lookups)

