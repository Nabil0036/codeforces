n=input()
#print(n)
l=len(n)
A=set('')
i=0
while i<l:
    A.add(n[i])
    i=i+1
#print(A)    
g=len(A)
#print(g)
if g%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')