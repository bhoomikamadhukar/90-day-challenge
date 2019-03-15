'''Sample Input

7 50
1 12 5 111 200 1000 10
Sample Output

4
Explanation

He can buy only 4 toys at most. These toys have the following prices:1,12,5,10 .'''

def maximumToys(prices, k):
    prices.sort()
    total = 0
    count = 0
    for i in prices:
        total = total + i
        if total <= k:
            count = count +1
    print (count)

def main():
	prices=int(input("enter price"))
	k=int(input("enter toy prices"))
	maximumToys(price,k)