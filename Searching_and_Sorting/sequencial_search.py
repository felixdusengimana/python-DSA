def seq_search(arr, elem):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == elem:
            found = True
        else:
            pos = pos + 1

    return found


print(seq_search([1, 2, 4, 5, 6, 7, 8, 10], 3))


def ordered_search(arr, elem):
    """Input array must be sorted."""
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == elem:
            found = True
        else:
            if arr[pos] > elem:
                stopped = True
            else:
                pos = pos + 1

    return found


print("with sorted: ", ordered_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
