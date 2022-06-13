def reverse(s):
    if len(s) == 1:
        return s

    return reverse(s[1:]) + s[0]


print(reverse("Hello This is a messaege from felix!"))