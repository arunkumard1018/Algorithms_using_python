


'''
 Input: N = 5
names[] = { "Geek", "Geeks", "Geeksfor",
  "GeeksforGeek", "GeeksforGeeks" }

Output: GeeksforGeeks
'''



def longest(names, n):
    dict = {}
    lst = []
    for i in names:
    	dict[len(i)] = i
    print(dict)
    #print(max(list(dict.items())))
    #print(list((dict.items())))
    for i in dict:
        lst.append(i)
    print(dict[max(lst)])


names = ["Geek", "Geeks", "Geeksfor","GeeksforGeek", "GeeksforGeeks"]
longest(names,len(names)-1)