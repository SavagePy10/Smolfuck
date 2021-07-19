import getch
a="".join(open(input(), "r").readlines())
b=-1
c=0
d=[0]*30000
e=0
while a<len(c)-1:
 b+=1
 if a[b]=="(":
  e+=1
  if e==1:
   if d[c]!=0:
    while e!=0:
     b+=1
     if a[b]=="(": e-=1
     elif a[b]==")": e+=1
  elif e==2:
   c+=1
  elif e==3: 
   if d[c]==255: d[c]=0
   else: d[c]+=1
 elif a[b]==")":
  e-=1
  if e==0:
   if d[c]==0:
    f=0
    while f!=0:
     if a[b]=="(": f-=1
     elif a[b]==")": f+=1
  elif e==1:
   if d[c]==0: b=0
  elif e==2:
   if d[c]==0: d[c]=ord(getch.getch())
   else: print(chr(d[c]))
