





#Merging of two arrays

def merge_2_arrays(a,b):
    i,j = 0,0
    c = []

    while i<len(a) and j<len(b) :
        
        if a[i] < b[j]:
            c.append(a[i])
            i += 1      
        else:
            c.append(b[j])
            j += 1
    while i<len(a):
        c.append(a[i])
        i+=1

    while j<len(b):
        c.append(b[j])
        j+=1
    return c

a = [2,4,6,8,10,25,45,65]
b = [1,3,5,7,9]
print(merge_2_arrays(a,b))
