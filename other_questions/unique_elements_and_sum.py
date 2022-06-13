# Given two integer arrays of size n, return a new array of
# size n such that n consists of only unique
# elements and the sum of all its elements is maximum.

def maximizedArray(arr1, arr2, n):
    combined = list(set(arr1 + arr2))
    return combined[-n:]


n = 5
arr1 = [7, 4, 10, 0, 1]
arr2 = [9, 7, 2, 3, 6]


print(maximizedArray(arr1, arr2, n))
