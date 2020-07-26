a=int(input())
c=[]
b=input().split()   
##print(b)
l=0
h=0
g=0
n=0
while n<a:
    h=int(b[n])
    g=g+h
    n=n+1
l=g/a
print(l)