'''you need to take exactly one element from the given list, not necessarily the largest element. 
You add the squares of the chosen elements and perform the modulo operation. 
The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers  and . 
The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.

 
 
Output Format

Output a single integer denoting the value of Smax. '''



n=int(input('enter number of lists'))
m=int(input('enter a number to divide'))
result=0
list1=[]
list2=[]
for i in range(n):
    inp=list(input('enter lists').split())
    inp=map(int,inp)
    list1.append(max(inp))
for j in list1:
    list2.append(j**2)
list2=sum(list2)
result=list2%m
print(result)