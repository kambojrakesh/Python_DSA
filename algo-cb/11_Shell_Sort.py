
arr = [12, 34, 54, 2, 3, 5, 2, 4, 1]
size = len(arr)
gap = size//2

while gap  > 0:
    for i in range(gap, size):
        anchor = arr[i]
        j = i
        while j >= gap and arr[j - gap] > anchor:
            arr[j] = arr[j - gap]
            arr[j - gap] = anchor
            j = j - gap

    gap = gap//2

print(arr)