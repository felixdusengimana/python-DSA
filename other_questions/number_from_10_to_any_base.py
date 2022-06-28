import math

# Convert number to any base from base 10


"""Takes number and base to which you want to convert it to,"""
reminders = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "C"}


def to_base(number: int, base: int):
    reminder = number % base
    if number < base:
        return number
    else:
        # Check for reminder in reminders to return A, B etc..
        if reminder in reminders:
            reminder = reminders[reminder]

        return str(to_base(math.floor(number / base), base)) + str(reminder)


print(to_base(2, 2))
