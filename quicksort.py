# Program to sort an array using quicksort
# quicksort is also called divide-and-conquer algorithm
# as well as comparison sort as it compares two elements and swap it.
# It works by selecting a 'pivot' element from an array
# and partitioning the other elements into two sun-arrays,
# ac to whether they are less than or greater than the pivot.
def quicksort(array):
    quicksort(array, 0, len(array)-1)

def quicksort2(low, high, array):
    if low < high:
        part = partition(low, high, array)
        quicksort2(low, part-1, array)
        quicksort2(low, part+1, array)

def get_pivot(low, high, array):

    mid = (high + low) // 2
    pivot = high

    if array[low] < array[mid]:
        if array[mid] < array[high]:
            pivot = mid
        elif array[low] < array[high]:
            pivot = low
        return pivot            
    
def partition(low, high, array):

    pivot_index = get_pivot(low, high, array)
    pivot_value = array[pivot_index]  
    
    array[pivot_index], array[low] = array[low], array[pivot_index]
    border = low

    for i in range(low, high + 1):
        if array[i] < pivot_value:
            border +=1
            array[i], array[border] = array[border], array[i]
    array[low], array[border] = array[border], array[low]        

    return (border)
  
