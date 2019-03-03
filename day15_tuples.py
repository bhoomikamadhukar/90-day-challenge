n=int(input('enter'))
integer_list = map(int, input('enter numbers').split())

list1=[]
for num in integer_list:
    list1.append(num)
hashing=tuple(list1)
print(hash(hashing))