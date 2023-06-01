#! /usr/bin/env python3
def quicksort(arr):
  if len(arr)<2:
    return arr
  idx = len(arr)//2
  pivot = arr[idx]
  smaller = []
  larger = []
  for i, v in enumerate(arr):
    if i!=idx:
      if v<=pivot:
        smaller.append(v)
      else:
        larger.append(v)
  return quicksort(smaller)+[pivot]+quicksort(larger)

print(quicksort([5,4,3,2,1]))
