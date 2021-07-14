lst = [2,5,4,6,3,7,1]



def buble_sort():
    for i in range(len(lst)):
        flag = 0 #to check if list is already Sorted 
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                flag += 1 #inc flag if list is not sorted
        if flag == 0: # checking if the Flag is zero
            return lst
    return lst

print(buble_sort())