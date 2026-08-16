
name = "Harry0123456789"

# print(name[0:2]) # goes from 0 to 2-1 ie 0 to 1

# print(name[2:-1]) # Same as name[2:4]

# print(name[0:10:n]) # Skip n- 1 characters
print(name[0:10:1]) # Skip 0 character
print(name[0:10:3]) # Skip 3-1 ie 2 characters

print(name[:4]) # Replace the first empty number with 0 # name[0:4]
print(name[1:]) # Replace the second empty number with length # name[1:15]

'''
% Another example String Slicing

% Slicing allows you to extract a portion of a string using the syntax string[start:stop:step].

text = "Hello, Python!"
print(text[0:5])   # Output: Hello
print(text[:5])    # Output: Hello (same as text[0:5])
print(text[7:])    # Output: Python! (from index 7 to end)
print(text[::2])   # Output: Hlo Pto!
print(text[-6:-1]) # Output: ython (negative indexing)

% Step Parameter

% The step parameter defines the interval of slicing.

text = "Python Programming"
print(text[::2])   # Output: Pto rgamn
print(text[::-1])  # Output: gnimmargorP nohtyP (reverses string)

% Practical Uses of Slicing

text = "Welcome to Python!"
print(text[:7])   # Output: Welcome
print(text[-7:])  # Output: Python!
print(text[3:-3]) # Output: come to Pyt

% String slicing is useful in many scenarios:

    Extracting substrings
    Reversing strings
    Removing characters
    Manipulating text efficiently

Summary

    1) Indexing allows accessing individual characters.
    2) Positive indexing starts from 0, negative indexing starts from -1.
    3) Slicing helps extract portions of a string.
    4) The step parameter defines the interval for selection.
    5) Using [::-1] reverses a string.

'''