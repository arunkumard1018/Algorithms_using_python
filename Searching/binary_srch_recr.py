#python program to search an element in Sorted array using Binary search

# Using Reccursive

lst = [3,6,8,12,13,17,25,29,31,36,42,47,53,55,62]

def binary_Search(low,high,key):
    if low==high:
        if key == lst[low]:
            return low
        else:
            return -1
    else:
        mid = (low+high)//2
        if key == lst[mid]:
            return mid
        elif key<lst[mid]:
            return binary_Search(low,mid-1,key)
        else:
            return binary_Search(mid+1,high,key)


key = int(input("Enter The Key Element To be search : "))
res = binary_Search(0,len(lst),key)

if res<0:
    print("Element Not Found")
else:
    print(f"The Key element {key} is present at index {res}")
