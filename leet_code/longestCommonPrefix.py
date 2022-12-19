from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    lowest_len = 0
    if len(strs[0]) < len(strs[1]) and len(strs[0]) < len(strs[2]):
        lowest_len = len(strs[0])
    elif len(strs[1]) < len(strs[0]) and len(strs[1]) < len(strs[2]):
        lowest_len = len(strs[1])
    else:
        lowest_len = len(strs[2])

    for idx, s in enumerate(strs[0]):
        if idx < lowest_len and s == strs[1][idx] and s == strs[2][idx]:
            prefix += s
        else:
            break

    return prefix


print(longestCommonPrefix(["dog","racecar","car"]))