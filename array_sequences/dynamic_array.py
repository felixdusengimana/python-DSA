import ctypes
import sys

class DynamicArray(object):
    """Dynamic array implementations."""

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            return IndexError("Item is out of bound!")

        return self.A[item]

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2*self.capacity)  # increase the capacity by 2x if it isn't enough

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):

        self.B = self.make_array(new_capacity)

        for k in range(self.n):
            self.B[k] = self.A[k]

        self.A = self.B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity*ctypes.py_object)()  # make an array based on new_capacity


# Implement Class

arr = DynamicArray()
for k in range(10):
    arr.append(k)
    print("1. Number if items in array: ", arr.__len__(), "with Size of: ", sys.getsizeof(arr))


arr2 = []
for k in range(10):
    arr2.append(k)
    print("2. Number if items in array: ", len(arr2), "with Size of: ", sys.getsizeof(arr2))