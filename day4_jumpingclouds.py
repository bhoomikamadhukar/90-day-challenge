def jumpingclouds(c):
    jump=0
    i=0
    while i<len(c)-1:
        if (i+2<len(c) and c[i+2]!=1):
            i+=1
        jump+=1
        i+=1
    print(jump)

def main():
    n=int(input('enter'))
    c=list(input('enter'))
    jumpingclouds(c)
main()