"""Consider the below example and make it more pythonic"""


lst = [1, 2, -5, 4]


def square(x):
    return x * x


def is_odd(x):
    return x % 2 == 1


# 1: Getting list of squares
result = map(square, lst)
final_result = list(result)
print(final_result)

res = []

for num in lst:
    res.append(square(num))

print(res)

# 2: Only getting the odd numbers
result1 = filter(is_odd, lst)
final_result_1 = list(result1)
print(final_result_1)

# 3: Creating a grid
num_rows = 2
num_columns = 3
grid = []

for _ in range(num_rows):
    curr_row = []

    for _ in range(num_columns):
        curr_row.append(0)

    grid.append(curr_row)

print(grid)


# Better approaches and important built-in functions
better_result = [square(num) for num in lst]
print(better_result)

better_result_1 = [num for num in lst if is_odd(num)]
print(better_result_1)

better_result_2 = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
print(better_result_2)

# Max
print(max)
print(max(1, 2, 3))
print(max([1, 2, -5, 4]))
print(max([1, 2, -5, 4], key=lambda x: x * x))

# Min
print(min)
print(min(1, 2, 3))
print(min([1, 2, -5, 4]))
print(min([1, 2, -5, 4], key=lambda x: x * x))

# Any: Would return if any of the iterable values are true
print(any)
print(any([1, 2, -5, 4]))
print(any([True, False]))
print(any([False, False]))
print(any([True, True]))
# any does not take any keyword value and so this will not work
# print(any([1, 2, -5, 4], key=lambda x: x % 2 == 1))
# instead we can use list comprehension

print(any([(lambda x: x % 2 == 1)(num) for num in [1, 2, -5, 4]]))

# All: Would return true if all of the iterable values are true
print(all([(lambda x: x % 2 == 1)(num) for num in [1, 2, -5, 4]]))
