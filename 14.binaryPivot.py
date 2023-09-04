def find_pivot(a):
    s, e = 0, len(a) - 1

    while s < e:
        m = (s + e) // 2

        if a[m] > a[0]:
            s = m + 1
        else:
            e = m

    return a[s]

# Example usage:
arr = [20, 30, 40, 50, 10]
pivot = find_pivot(arr)
print("The pivot element is:", pivot)
