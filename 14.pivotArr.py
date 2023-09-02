def pivArr(a,n):  
  s=0
  l=0
  for i in range(0,n):
    s=s+a[i]
  for i in range(0,n):
    if l==s-a[i]-l:
      return i
    l=l+a[i]
  return -1
a=[1,7,3,6,5,6]
n=len(a)
print(pivArr(a,n))
  
