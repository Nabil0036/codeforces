b=input()
n=list(b)
#print(n)
j=n
#print(j)
l=len(n)
g=[]
i=0
lu=0
q=n.count('1')
if q!=l:
    rt=b.find('0')
    del n[rt]
    kuli=''.join(n)
    print(kuli)
#print(yu[2:h+1])
elif q==l:
    del n[l-1]
    dy=''.join(n)
    print(dy)