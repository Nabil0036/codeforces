a=input()
b=list(a)
#print(b)
n=len(b)
#print(n)
F=[]
Q=0
q=0
v=0
while v<n:
    x=ord(b[v])
    if x>=60 and x<=90:
        Q=Q+1
    elif x>=90 and x<=122:
        q=q+1
    v=v+1
if Q>q:
    print(a.upper())
elif Q==q:
    print(a.lower())
else:
    print(a.lower())