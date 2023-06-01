#! /usr/bin/env python3
import math

def crystal_balls(arr):
  jmp = int(math.sqrt(len(arr)))
  i = 0
  while i<len(arr)-jmp:
    if arr[i]:
      break
    i+=jmp
  while arr[i]:
    i-=1
    if i<0:
      break
  if arr[i+1]:
    return i+1
  return -1

print(crystal_balls([0,0,0,1]))
