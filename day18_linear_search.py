def linear_search(n,ar,find):
    for i in range(0,n):
        if (ar[i]==find):
            return i 
    return -1


def main():
    n=int(input('enter no of array elements'))
    ar = list(map(int, input("enter array elements").rstrip().split()))
    find=int(input('enter element to search'))
    res=linear_search(n,ar,find)
    if (res==-1):
        print("element not found in array")
    else:
        print(f"element found at index:",res)
main()