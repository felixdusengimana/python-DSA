def pair_sum(int_list, desired_sum):
    if len(int_list) < 2:
        return

    # set for tracking
    seen = set()
    output = set()

    for num in int_list:
        target = desired_sum - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print("\n".join(map(str, list(output))))
    return len(output)


arr = [6, 0, 1, 3, 2, 2, 4, -2]
print(f"There are {pair_sum(int_list=arr, desired_sum=4)} pairs.")
