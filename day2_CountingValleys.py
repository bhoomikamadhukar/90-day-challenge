def CountingValleys(n,s):
    up=0 
    down=0 
    for i in range(n):
        if(s[i]=='D'):
            down+=1 
            if(down==0):
                up+=1
        else:
            down-=1
        
    print (up)

def main():
    n=int(input("enter number of steps"))
    s=list(input("enter step sequence"))
    CountingValleys(n,s)
main()