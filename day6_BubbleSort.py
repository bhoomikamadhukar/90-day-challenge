def countSwaps(n,a):
    count = 0
    temp=0
    for i in range(0,n):
        for j in range(0,n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                count+=1
    print(count)

def main():
    n=int(input('enter n'))
    a=list(input('enter elements'))
    countSwaps(n,a)
main()
    