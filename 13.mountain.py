class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
      s=0
      e=len(arr)-1
      m=(s+e)//2

      while s<=e:
        if arr[m]>arr[m-1] and arr[m]>arr[m+1]:
          return m
        elif arr[m-1]<arr[m] :
          s=m+1
        elif  arr[m]>arr[m+1]:
          e=m
    
        m=(s+e)//2  #later replace with s+(e-s//2)
      return -1
