#! /usr/bin/env python3
def bubblesort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1-i):
      if arr[j+1]<arr[j]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr

print(bubblesort([5,4,3,2,1]))
