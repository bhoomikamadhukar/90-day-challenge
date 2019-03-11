'''Sample Input

AABCAAADA
3   
Sample Output

AB
CA
AD'''





def merge_the_tools(string, k):
    n=len(string)

    for i in range(0, n, k):
        slicedStr = string[i : i+k]
        list1 =[]
        for y in slicedStr:
            if y not in list1:
                list1.append(y)
        print (''.join(list1))

def main():
    string, k = input("enter string"), int(input("enter number"))
    merge_the_tools(string, k)
main()