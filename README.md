# TRUR1282-23-24

Algorithms for the Maths for Computing module at Truro College

The main program is `sort_timer.py` which runs various sorting
algorithms with random arrays for data of various lenghts.

## Updown sort

This algorithm was inspired by looking at student work who managed to find
the worse case for quicksort with an ordered list.
Could we write an algorithm that worked well when the data was partially sorted?
The main algorithm works by scanning the input look for increasing or decreasing sequences and then merger those sequences.
If for example the input list was

```
[1, 2, 3, 5, 8, 7, 4, 2, 5, 3]
```

it would devided into sequences

```
[1, 2, 3, 5, 8], [7, 4, 2], [5], [3]
```

The code for this is relativly simple:

```
def updown_sort(arr,merger):
    """Sort the array arr using the up-down sort algorithm and
    a given merging algorithm.
    Args:
        arr: The array to sort.
        merger: The merging algorithm to use.   """
    global max_queue_size
    dir = 1
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
```

It is suplied with a merging algorithm with two methods
 `merge(work)` to add a new subsequence to the merge routine, and `collapse()` which returns the final sorted list. Several different implementation of these algorithm have been tried. Each is a subclass of `Merger`.

The first version, `SimpleMerger` simply kept a sorted list, at each call to `merge` it
simply merged the existing and new lists, and `collapse` just returns the already sorted list. This has O(n^2) complexity.

The second version, `IncreasingLengthMerger`, contains a list of
of sorted sequences. Each sequence is longer than the previous one.
For example [ [1], [2,3], [4,5,6,7,8]].
When a new sequence is merged each item in the list is compared with
the input sequence. If length of the item is
or equal the length of the input sequence then the item is removed from the list and merged with the input sequence. Otherwise the loop exits.
Finally the input sequence is inserted at the front of the list.

For example if the input is [9] it is first compared with [1], their lengths
are the same, so they are merged to form [1,9], and the list [1] removed from the queue. It is then compared with [2,3] again they are merged to form [1,2,3,9]. In the next comparision the input is shorter, so it is pushed to the from of the queue: [[1,2,3,9], [4,5,6,7,8]]. This has better complexity, probably O(n log n).

In python this algorithm has potential problems with list operations, the `insert(x,0)` operation is O(n). This is not a big issue at even with a million items the queue only grows to 28 elements. One alternative is to use the [deque](https://docs.python.org/3/library/collections.html#deque-objects) collection.
This has O(1) compexity for operations at both ends of the list. `DequeMerger` operates like `IncreasingLengthMerger` but uses a deque internally. It can be a little bit faster.

A final version `TreeMerger` mirror the tree structure you find with merge sort.
Conceptually it works as a binary tree built from the bottom up. Elements are added at the bottom of a binary tree, the parent of each pair contains the result of merging the two children. So the top of the tree contains the sorted list. In practice we don't need the whole tree, as soon as two child nodes are present the parent can be calculate and the children removed. The partially compleated tree can be represented as an array where the i-th element
is the node at height i, measured from the bottom. This can either be a sorted list or None, if its parent has been calculated.

Consider repeatidly adding sequences [a],[b],[c],[d].
The list is intially empty [], after adding [a] it is [[a]].
After adding [b] it is [None,[a,b]], first [b] is merged with [a]
the first element set to None, and the merged list [a,b]
added at the end of the queue. Adding [c] sets the first element to None
giving [[c],[ab]]. Adding [d] first merges it with [c], giving the list
[cd], the first element is set to None and
the second elements is tested. A second merge is performed and the result
[abcd] is added to end of the queue, giving a final queue of [None,None,[abcd]].

### Comparing performance

To analyise the performance of the different merger we can look at how many times
each algorithm calls the `mergeArray(left,right)` method. The number of iterations of this method
it the sum of the lengths of the two arguments.

For the `SimpleMerger` we merge each input into a list of increasing lengths.

| Step  | argument to merge  | inputs to mergeArray | len(left) | len(right) | num itts | culumative itts |
|-------|--------------------|---------------------|----------|---------|------|-------------|
| 1     | [a]  |   [],[a]            |   0      |    1    |  1   |       1     |
| 2     | [b]  |  [a],[b]            |   1      |    1    |  2   |       3     |
| 3     | [c]  |  [a,b],[c]          |   2      |    1    |  3   |       6     |
| 4     | [d]  |  [a,b,c],[d]        |  3       |    1    |  4   |      10     |
| 5     | [e]  | [a,b,c,d],[e]       |  4       |    1    |  5   |      15     |
| 6     | [f]  |  [a,b,c,d,e],[f]    |   5      |    1    |  6   |      21     |
| 7     | [g]  | [a,b,c,d,e,f],[g]   |   6      |    1    |  7   |      28     |
| 8     | [h]  | [a,b,c,d,e,f,g],[h] |   7      |    1    |  8   |      36     |

The culumative number of itterations are the triangular numbers n(n+1)/2, so we see the algorithm has order O(n^2).

Merge sort would sort the data in pairs, this it

| Step  |  Inputs          | len (left) | len(right) | num itts   |  culm itts |
|------ |------------------------|------|-------|-------|----------|
| 1     |   [a],[b]              |  1   |   1   |   2   |       2  |
| 2     |   [c],[d]              |  1   |   1   |   2   |       4  |
| 3     |   [e],[f]              |  1   |   1   |   2   |       6  |
| 4     |   [g],[h]              |  1   |   1   |   2   |       8  |
| 5     |   [a,b],[c,d]          |  2   |   2   |   4   |      12  |
| 6     |   [e,f],[g,h]          |  2   |   2   |   4   |      16  |
| 7     |   [a,b,c,d],[e,f,g,h]  |  4   |   4   |   8   |      24  |

For this dataset
`IncreasingLengthMerger` and `TreeMerger` performs the same set of merges but in a different order.

| Step  | argument to merge |  Inputs to mergeArray | len (left) | len(right) | num itts   |  culm itts |
|-------|------|--------------------|------|-------|-------|----------|
| 1     |  [a] | | | | | |
| 2     |  [b] |  [a],[b]              |  1   |   1   |    2  |       2  |
| 3     |  [c] | | | | | |
| 4a    |  [d] | [c],[d]              |  1   |   1   |   2   |       4  |
| 4b    |      | [a,b],[c,d]          |  2   |   2   |   4   |       8  |
| 5     |  [e] | | | | | |
| 6     |  [f] | [e],[f]              |  1   |   1   |   2   |      10  |
| 7     |  [g] | | | | | |
| 8a    |  [h] | [g],[h]              |  1   |   1   |   2   |      12  |
| 8b    |      | [e,f],[g,h]          |  2   |   2   |   4   |      16  |
| 8c    |      | [a,b,c,d],[e,f,g,h]  |  4   |   4   |   8   |      24  |
