"""Sets and why they are important"""

# Without using a set()
def count_unique_list(s):

    # Using list will cause the look-up
    # time to be O(n)
    seen_c = []

    for c in s:  # O(n) because of for-loop
        if c not in seen_c:  # O(n) becuase of look-up time in a list
            seen_c.append(c)  # O(1)

    return len(seen_c)  # O(n^2)


# With using set()
def count_unique_set(s):

    # Sets are like dictionaries with restrictions
    seen_c = set()

    for c in s:  # O(n) because of for-loop
        if c not in seen_c:  # O(1) because look-up in dictionary is constant
            seen_c.add(c)  # O(1)

    return len(seen_c)  # O(n)


str1 = "aabbcc"
str2 = "abcdef"

print("Using lists\n")
print(count_unique_list(str1))
print(count_unique_list(str2), "\n\n")

print("using sets as function\n")
print(count_unique_set(str1))
print(count_unique_set(str2), "\n\n")


# Using set comprehension
def count_unique(s):
    return len({c for c in s})  # O(n)


str3 = "rtuhdfjbs"
print("using set comprehension\n")
print(count_unique(str3))
print(count_unique(str1))
print(count_unique(str2), "\n\n")


# Using set in real projects
def count(s):
    return len(set(s))  # O(n)


str4 = "sgfiuerkjneag"


print("Using sets in real projects\n")
print(count(str4))
print(count(str1))
print(count(str2))
print(count(str3), "\n\n")
