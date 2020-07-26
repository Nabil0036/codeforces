import math
from itertools import groupby

n=int(input())
i=0
q=[]
while i<n:
    l=input().split(' ')
    w=l[0]+l[1]
    q.append(w)
    i+=1
#print(q)
h=len(q)    
j=0
p=0
z=0
b=[]
b=[len(list(group)) for key,group in groupby(q)]
#print(b)
b.sort()
k=len(b)
print(b[k-1])
 