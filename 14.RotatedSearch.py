def searchRotated(a,n,k):
    s=0
    e=n-1
    while s<=e:
        m=(s+e)//2
        if a[m]==k:
            return m
        if a[s]<=a[m]:
            if a[s]<=k<=a[m]:
                e=m-1
            else:
                s=m+1
        else:
            if a[m]<=k<=a[e]:
                s=m+1
            else:
                e=m-1
arr=[7,8,9,1,2,3,4,5,6]
n=len(arr)
k=1
print(searchRotated(arr,n,k))
