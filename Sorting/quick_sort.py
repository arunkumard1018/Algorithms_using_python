
arr = [ -6,-8,0,10, 7, 8, 9, 1, 5 ]     

# This Function handles sorting part of qick Sort
def partition(start,end,arr):

    # Initializing pivot with starting Element
    pivot_index = start
    pivot  = arr[pivot_index]

    # This Loop runs still start pointer cross end pointer
    # and when it does we swap the pivot with element on end pointer
    while start<end:

        # increment the start pointer till it find element greater then pivot
        while start < len(arr) and arr[start] <= pivot :
            start += 1
        # Decrement The end pointer till it finds element lesser then pivot
        while end >= -1 and arr[end] >= pivot:
            end -= 1
        # if start and end not crossed each other swap the elements on start and end
        if start < end:
            arr[start],arr[end] = arr[end],arr[start]
    #swap pivot with elemen o end pointer
    arr[pivot_index],arr[end] = arr[end],arr[pivot_index]
    #returning end pointer to divide the array ionto two
    return end

def quick_sort(start,end,arr):
    if start < end:
        p = partition(start,end,arr)
        # sort elements before partition and after partition
        quick_sort(start,p-1,arr)
        quick_sort(p+1,end,arr)

quick_sort(0,len(arr)-1,arr)
print(arr)
