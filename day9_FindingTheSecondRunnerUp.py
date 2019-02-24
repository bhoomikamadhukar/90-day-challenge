n=int(input('enter n'))
list1=[]
arr = map(int, input('enter array').split())
for j in arr:
    if j not in list1:
        list1.append(j)
list1.remove(max(list1))
print(max(list1))