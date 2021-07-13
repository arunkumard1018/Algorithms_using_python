lst = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]



def linear(key):
    for i in range(len(lst)):
        if lst[i]==key:
            return i
    return -1

key = int(input("Enter The Key Element to be Search  : "))
result = linear(key)

if result<0:
    print("Element Not Found")
else:
    print(f"The Key element {key} is present at index {result}")