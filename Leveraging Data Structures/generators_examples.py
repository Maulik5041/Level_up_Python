"""Generators are used to save memory"""


import sys


g = (i for i in range(6))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# This should throw an error as there are no more values to iterate
# print(next(g))


# For adding all the values from 1 to 1000 using list
print(sum([i for i in range(1, 1001)]))


# For adding the same values using a generator
print(sum((i for i in range(1, 1001))))


# To understand the difference, look at the memory consumption
lst = [i for i in range(1, 1001)]
print(sys.getsizeof(lst))

gens = (i for i in range(1, 1001))
print(sys.getsizeof(gens))


# The difference between lists and generators is not only
# in the given example. But if we go on increasing the
# range, it would virtually remain the same

print(sys.getsizeof((i for i in range(1, 100100))))
print(sys.getsizeof((i for i in range(1, 10010000))))
print(sys.getsizeof((i for i in range(1, 1001000000))))
print(sys.getsizeof((i for i in range(1, 10010000000000))))


"""
Thus if there is a function that takes a value and passes
it into the function one at a time, then using a list will
cause the function to run very slowly. Instead, using a
generator can be very effective. To do that, instead of using
return, we will use yield.
"""


def f():
    yield 1
    yield 2
    yield 3


print(f())

# It is important to assign the function to a variable
g = f()
print(next(g))
print(next(g))
print(next(g))

# If not assigned to a variable, the function will create
# a new generator every time its called
print(next(f()))
print(next(f()))
print(next(f()))
