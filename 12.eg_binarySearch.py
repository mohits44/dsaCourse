def bs(arr, key):
    n=len(arr)
    low=0
    high=n-1
    
 
    while low<=high:
        mid=(low+high)//2     #later replace with low+(high-low//2)
        if key==arr[mid]:
            return mid
        else:
            if key>arr[mid]: #right dabba
                low=mid+1
            else:
                high=mid-1
   
    return -1
  
a=[2,4,6,8,10]
key=10
print(bs(a,key))
