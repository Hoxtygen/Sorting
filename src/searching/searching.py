# STRETCH: implement Linear Search
def linear_search(arr, target):
  arrLen = len(arr)
  # TO-DO: add missing code
  for i in range(arrLen):
      if target == arr[i]:
          return 1;

  return -1   # not found

print(linear_search([2, 4, 6, 9, 5], 100))

# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
