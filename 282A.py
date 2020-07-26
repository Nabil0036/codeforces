n=int(input())
k=0
i=0
while i<n:
    s=input()
    if s=='X++' or  s=='++X':
        k=k+1
    else:
        k=k-1
    i=i+1
    
print(k)