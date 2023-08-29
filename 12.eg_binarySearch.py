def bs():
  n=5
  s=0
  e=n-1
  mid=s+e//2     #later replace with s+(e-s//2)
  a=[2,4,6,8,10]
  key=2
  while s<=e:
    if key==a[mid]:
      return mid
    else:
      if key>a[mid]: #right dabba
        s=mid
      else:
        e=mid
    mid=(s+e)//2  #later replace with s+(e-s//2)
  return -1
print(bs())
     
      
