s = "hello world" # Strings are immutable

# s[0] = "R" # You cannot do this

a = len(s)
print(a)
print(s.upper(), s)
print(s.lower())
print(s.capitalize())
print(s.title())

# text = " \nhello world "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world "
# print(text.rstrip()) # Output: " hello world"


text = "Python is fun and fun and fun"
print(text.find("is")) # Output: 7 Index of first occurence
print(text.replace("fun", "awesome")) 


text = "Apples,Bananas,Pineapples"
print(text.split(","))
print(",".join(['Apples', 'Bananas', 'Pineapples']))

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False

'''
Common String Methods:-

Changing Case:

text = "hello world"
print(text.upper())      # Output: "HELLO WORLD"
print(text.lower())      # Output: "hello world"
print(text.title())      # Output: "Hello World"
print(text.capitalize())  # Output: "Hello world"

Removing Whitespace:

text = "  hello world  "
print(text.strip())  # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"

Finding and Replacing:

text = "Python is fun"
print(text.find("is"))   # Output: 7
print(text.replace("fun", "awesome"))  # Output: "Python is awesome"

Splitting and Joining:

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']
new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"

Checking String Properties:

text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False

Useful Built-in String Functions:

len() - Get Length of a String

text = "Hello, Python!"
print(len(text))  # Output: 14

ord() and chr() - Character Encoding

print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'

'''
