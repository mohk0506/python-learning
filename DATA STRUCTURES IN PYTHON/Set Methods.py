s = {3, 23, 2, 11}

print(s, type(s))
# print(s[3]) # You are not allowed to do something like this

s = {34, 23, 1, 3, 22}

print(s)

s.add(32)
s.add(322)
s.remove(1)
# s.remove(434234) # Throws an error
s.discard(42323)
print(s)

a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b) # Contains all the elements in a along with all the elements in b
print(c)

d = a.intersection(b) # Contains only the elements that are present in a as well as b
print(d)

