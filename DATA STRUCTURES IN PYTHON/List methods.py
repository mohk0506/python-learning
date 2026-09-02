
Limarks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

print(marks)
# marks.append(63) # This will change the original list
# marks.pop()
marks.extend(extra_marks)
print(marks)

# Create a list containing the table of 5


# table = []

# for i in range(1, 11):
#     table.append(5*i)

table = [5*i for i in range(1, 11)]

print(table)

