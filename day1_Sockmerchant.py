def sockMerchant(n, ar):
    count = 0
    ar.sort()
    i = 0
    for i in range(0,n):
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    print(count)

def main():
    n=int(input('enter the number of socks'))
    ar=list(input('enter the pairs'))
    sockMerchant(n,ar)
    
main()
