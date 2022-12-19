# The question is to swap two values in a array/list
# that follow each other_questions
# ex: swap([1,2,3,4]) => [2,1,4,3]

# swap function
def swap(arr, index: int):
    temp = arr[index]
    arr[index] = arr[index - 1]
    arr[index - 1] = temp


def swapPairs(el):
    for idx, i in enumerate(el):
        if (idx+1) % 2 == 0:
            swap(el, idx)

    return el


print(swapPairs([1, 2, 3, 4]))
