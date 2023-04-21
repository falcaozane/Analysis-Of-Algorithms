def findMinMax(a, low, high):
    if high == low:
        return a[low], a[low]
    elif low+1 == high:
        if a[low] < a[high]:
            return a[low], a[high]
        else:
            return a[high], a[low]
    else:
        mid = (low + high)//2
        minL, maxL = findMinMax(a, low, mid)
        minR, maxR = findMinMax(a, mid+1, high)

        minimum = min(minL, minR)
        maximum = max(maxL, maxR)

        return minimum, maximum

a = list(map(int, input("Enter the elements of the array separated by space: ").split()))
n = len(a)
min_val, max_val = findMinMax(a, 0, n-1)
print(f"The minimum element is: {min_val}\nThe maximum element is: {max_val}")

