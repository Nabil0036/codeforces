a=input()
l=len(a)
h=ord(a[0])
j=[]
k=a[0]
if h in range(65,91):
    print(a)
if h in range(95,123):
    e=h-32
    f=chr(e)
##    print(f)
    j.append(f)
    i=1
    while i<l:
        j.append(a[i])
        i=i+1
    k=''.join(j)
    print(k)