import collections


def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


arr1 = [5, 5, 7, 7]
arr2 = [5, 5, 7, 7]
print(finder(arr1, arr2))

#
# def finder2(arr1, arr2):
#     d = collections.defaultdict(int)
#     for num in arr1:
#         d[num] += 1
#     i = 0
#     for num in arr2:
#         i += 1
#         # print(i,".", d, "num: ", num)
#         if d[num] == 0:
#             return num
#
#         else:
#             d[num] -= 1
#
#
# print(finder2(arr1, arr2))
