# Online Python-3 Compiler (Interpreter)
def bs():
  n=5
  s=0
  e=n-1
  m=s+e//2     #later replace with s+(e-s//2)
  a=[2,8,6,4,2]
  
  while s<=e:
    if a[m]>a[m-1] and a[m]>a[m+1]:
      return m
    elif a[m-1]<a[m] and a[m]<a[m+1]:
        s=m+1
    elif a[m-1]>a[m] and a[m]>a[m+1]:
        e=m
    
    m=(s+e)//2  #later replace with s+(e-s//2)
  return -1
print(bs())
