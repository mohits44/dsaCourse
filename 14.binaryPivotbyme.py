def binaryPivot(a,n):
    s=0
    e=len(a)-1
    m=(s+e)//2
    ans=0
    while(s<e):
        if a[m]>=a[0]:
            s=m+1
        else:
            e=m
        m=(s+e)//2
    return a[s]
arr = [50, 10, 20, 30, 40]
pivot = binaryPivot(arr, len(arr))
print("The pivot element is:", pivot)
