# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

def urlify(url: str, length: int):
    # make url equal to given length
    url = url.split(" ")
    return "%20".join(url)


print(urlify("hello world there!", 13))
