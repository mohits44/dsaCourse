# def findArrayIntersection(arr: list, n: int, brr: list, m: int):
#     lst=[]
#     for i in range(0,n):
#         element=arr[i]
#         for j in range(0,m):
#             if element==brr[j]:
#                 lst.append(element)
#                 brr[j]=-2
#                 break
#     return lst

# optimised solution by chatGPT
def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    lst = []
    brr_set = set(brr)  # Convert brr to a set for faster lookups

    for element in arr:
        if element in brr_set:
            lst.append(element)
            brr_set.remove(element)  # Remove the element from the set to avoid duplicates

    return lst


# Example usage
arr = [7]
brr = [4, 5, 6, 7]
n = len(arr)
m = len(brr)
intersection = findArrayIntersection(arr, n, brr, m)
print("Intersection:", intersection)
