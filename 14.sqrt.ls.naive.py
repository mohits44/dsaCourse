def bs():
  

  
      #later replace with s+(e-s//2)
  i=1
  key=16
  while i*i<=key:
    if key==i*i:
      return i
    else:
      if key>i*i: #right dabba
        i=i+1
        continue
      else:
        return i
  
print(bs())
     
