def sockMerchant(n, ar):
    count=0
    ar.sort()
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count+=1
            i+=2
        else:
            i+=1
    print(count)

def main():
    n=int(input('enter the number of socks'))
    ar=list(input('enter the pairs'))
    sockMerchant(n,ar)
    
    
main()