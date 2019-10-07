# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
  arrLen = len(arr)
  for i in range(arrLen -1):
    cur_index = i
    smallest_index = cur_index
    for j in range(cur_index, arrLen):
      if arr[j] < arr[smallest_index]:
        smallest_index = j
    arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
  return arr

print(selection_sort([5, 3, 6, 2, 10]))




# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arrLen = len(arr)
    sorted = False
    while not sorted:
        num_of_swaps = 0
        for k in range(0, arrLen-1):
            if arr[k] > arr[k+1]:
                num_of_swaps += 1
                placeholder = arr[k+1]
                arr[k+1] = arr[k]
                arr[k] = placeholder

        if not num_of_swaps:
            sorted = True
    return arr

print(bubble_sort([5, 3, 6, 2, 10]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
