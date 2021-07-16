

def merge(arr,low,high,mid):
    i = low
    j = mid
    lst = []

    while i<mid and j<high:
        
        if arr[i] < arr[j]:
            lst.append(arr[i])
            i += 1
        else:
            lst.append(arr[j])
            j += 1
        
    while i < mid:
        lst.append(arr[i])
        i+=1
    
    while j < high:
        lst.append(arr[j])
        j += 1
    
    return lst

arr = [2,1]
print(merge(arr,0,len(arr),len(arr)//2))