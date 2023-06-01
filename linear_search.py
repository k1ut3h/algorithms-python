#! /usr/bin/env python3
def linear_search(arr, val):
  for i, v in enumerate(arr):
    if v==val:
      return i
  return -1

print(linear_search([3,4,2,6,7],7))
