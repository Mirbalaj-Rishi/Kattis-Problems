import random

# make a list of 200 random numbers

L = []
for i in range(200):
    x = random.randint(0, 1000)
    L.append(x)
print("Unsorted List: ")
print(L)

# Throw all numbers into the heap
print()
import heapq
Heap = []
for i in range(200):
    x = L[i]
    heapq.heappush(Heap, x)
print("Heap")
print(Heap)

# Pop all numbers out of the heap

print()
Sorted = []
for i in range(0,200):
    x = heapq.heappop(Heap)
    Sorted.append(x)
print("Sorted List")
print(Sorted)
