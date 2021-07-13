#python program to search an element in Sorted array using Binary search

lst = [3,6,8,12,13,17,25,29,31,36,42,47,53,55,62]


def binary_Srch(key):
    low = 0
    high = len(lst)
    while low<high:
        mid = (low+high-1)//2
        if key == lst[mid]:
            return mid
        if key < lst[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1


key = int(input("Enter The Key Element To be search : "))
res = binary_Srch(key)

if res<0:
    print("Element Not Found")
else:
    print(f"The Key element {key} is present at index {res}")
    