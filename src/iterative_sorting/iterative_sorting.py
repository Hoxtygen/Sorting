# TO-DO: Complete the selection_sort() function below
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    return arr

def selection_sort( arr ):
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        for j in range(i+1, len(arr)):
          if(arr[i] > arr[j]):
            swap(arr, cur_index, j)
    return arr

print(selection_sort([5, 3, 6, 2, 10]))




# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
