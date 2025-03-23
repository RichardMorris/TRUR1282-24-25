# TRUR1282-23-24
Algorithms for the Maths for Computing module at Truro College

The main program is `sort_timer.py` which runs various sorting 
algorithms with random arrays for data of various lenghts.

# Updown sort

This algorithm was inspired by looking at student work who managed to find 
the worse case for quicksort with an ordered list. 
Could we write an algorithm that worked well when the data was partially sorted.
The main algorithm works by scanning the input look for increasing or decreasing sequences and then merger those sequences.
If for example the input list was
```
[1, 2, 3, 5, 8, 7, 4, 2, 5, 3]
```
it would devided into sequences
```
[1, 2, 3, 5, 8], [7, 4, 2], [5], [3]
```