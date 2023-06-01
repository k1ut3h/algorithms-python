#! /usr/bin/env python3
def binary_search(arr, val):
  arr = sorted(arr)
  lo = 0
  hi = len(arr)

  while hi>lo:
    mid = (lo+hi)//2
    if arr[mid]==val:
      return mid
    elif arr[mid]>val:
      hi = mid
    else:
      lo = mid+1
  return -1

print(binary_search([3,4,2,6,7],4))
