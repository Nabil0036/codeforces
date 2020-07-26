a= input().split(" ")
#print(a)
n=int(a[0])
k=int(a[1])
#print(n,k)
q=input()
w=set(q)
e=list(w)
l=len(e)
i=0
t=[]
#print('q',q)
#print('e',e)
while i<l:
    r=e[i]
    y=q.count(r)
    t.append(y)
    i+=1
#print('t',t)
t.sort()
t.reverse()
#print(t)
c=list(set(t))
c.sort()
c.reverse()
#print(c)
v=len(t)
b=0
m=0
bn=0
while b<v:
    nj=t[b]
    #print('.')
    #print('nj',nj)
    if nj<k:
        #print('yes')
        m=m+nj*nj
        k=k-nj
        #print(k,m)
    elif k==0:
        #print('ll')
        break
    elif k<nj:
        #print('kk')
        m=m+k*k
        break
    elif k==nj:
        m=m+nj*nj
        k=k-nj
        
    b+=1    
print(m)    
##x=k-z
##print(z*z+x)