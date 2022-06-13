def binary_search(arr, elem):
    """Binary Search."""
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) / 2
