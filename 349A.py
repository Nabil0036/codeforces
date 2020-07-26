k=input()
n=input().split( )
#print(n)
l=len(n)
x=0
y=0
z=0
g=0
h=0
i=0
if n[0]=='25':
    while i<l:
        if n[i]=='25':
            x=x+1
        
        if n[i]=='50':
            y=y+1
            x=x-1
            if x<0:
                break
            
        
        if n[i]=='100':
            z=z+1
            if y>=1 and x>=1:
                y=y-1
                x=x-1
            elif x>=3:
                x=x-3
        
            else:
                break
        
        i=i+1
    if i==l:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
#print(x,y,z,'g =',g,'i=',i)