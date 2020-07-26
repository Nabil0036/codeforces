y1,k1,n1=input().split()
y=int(y1)
k=int(k1)
n=int(n1)
#print(y,k,n)

b=0
f=[]
j=0
x=k-y
l=n-y
if y<n:
    if k!=y and k!=n and x>=0:
        b=x
        while j<l:
            j=j+b
            #print(j)
            c=j+y
            if c<=n:
                f.append(j)
            j+=k-b
        h=len(f)
        if h==0 or f[0]==0:
            print('-1')
        elif h>0 :
            print(*f)
       

    elif k!=y and k!=n and x<0 :
    ##    print('k')
        while True:
            if x>0:
                break
    ##        print('j')
            x+=k
        b=x  
    ##    print(x)
        while j<l:
            j=j+b
            #print(j)
            c=j+y
            if c<=n:
                f.append(j)
            j+=k-b
        h=len(f)
        if h==0 or f[0]==0:
            print('-1')
        elif h>0 :
            print(*f)
    elif n==2*y and k!=n and x==0:
        print(n-y)
    elif k==n:
        print(n-y)
    elif k>n:
        print('-1')        
else:
    print('-1')