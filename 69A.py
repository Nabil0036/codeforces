n=int(input())
F=[]
Q=[]
X=0
Y=0
Z=0
j=0
m=0
while m<n:
    x, y, z=map(int,input().split())
    F=[x,y,z]
    Q.append(F)
    m=m+1
#print(Q)
k=0
while k<n:
    
    X=X+Q[k][0]
    Y=Y+Q[k][1]
    Z=Z+Q[k][2]
    k=k+1
#print(X,Y,Z)
if X==0 and Y==0 and Z==0:
    print("YES")
else:
    print("NO")