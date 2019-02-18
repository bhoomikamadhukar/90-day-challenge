'''John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in . 
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Output Format

Return the total number of matching pairs of socks that John can sell.'''

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