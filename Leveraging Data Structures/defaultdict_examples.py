"""Using dicionaries in a much more efficient way"""


from collections import defaultdict


student_grades = {
    "Jack": [85, 90],
    "Jill": [80, 95]
}


def get_grades_naive(name):
    if name in student_grades:
        return student_grades[name]

    return []


print("\nGetting grades naively")
print(get_grades_naive("Jack"))
print(get_grades_naive("Jill"))
print(get_grades_naive("Joe"))
print(student_grades, "\n")


def get_grades_better(name):
    return student_grades.get(name, [])


print("Getting grades efficiently using get method")
print(get_grades_better("Jack"))
print(get_grades_better("Joe"))
print(student_grades, "\n")


def get_grades_with_asssignment(name):
    if name not in student_grades:
        student_grades[name] = []

    return student_grades[name]


print("Getting grades and assigning new keys as well")
print(get_grades_with_asssignment("Jack"))
print(get_grades_with_asssignment("Joe"))
print(student_grades, "\n")


def get_grades_with_assignment_better(name):
    return student_grades.setdefault(name, [])


print("Getting grades and assigning new keys efficiently")
print(get_grades_with_assignment_better("Jack"))
print(get_grades_with_assignment_better("Jill"))
print(get_grades_with_assignment_better("Jonah"))
print(student_grades, "\n")


def set_grade_naive(name, score):
    if name in student_grades:
        grades = student_grades[name]

    else:
        student_grades[name] = []
        grades = student_grades[name]

    grades.append(score)


print("Setting new grades naively")
set_grade_naive("Jack", 100)
set_grade_naive("Joe", 100)
print(student_grades, "\n")


def set_grade_better(name, score):
    grades = get_grades_with_assignment_better(name)
    grades.append(score)


print("Setting new grades in a better way")
set_grade_better("Jack", 55)
set_grade_better("Jill", 75)
print(student_grades, "\n")


# The main strength of defaultdict
student_grades = defaultdict(list, student_grades)


def set_grade_best(name, score):
    student_grades[name].append(score)


print("Default dict usage")
print(student_grades)
set_grade_best("Jonah", 80)
set_grade_best("Jill", 78)
print(student_grades)
print(student_grades['Jonah'], "\n")

print("Setting default score of students to 70")
student_score = defaultdict(lambda: 70)
print(student_score)
print(student_score["Jack"] + 10, "\n")
print("Scores of Jack will still remain only 70 as it's value has not been changed")
print(student_score, "\n")
print(
    f"To actually change the value we need to do this: student_score['Jack'] += 10")
student_score["Jack"] += 10
print(student_score)
student_score["John"] += 15
print(student_score)
