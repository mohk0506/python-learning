a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a charger")
    case 3:
        print("You won $3")
    case 6:
        print("You won a camera")
    case _:
        print("Better luck next time")
    

'''
Syntax:
match value:
    case pattern1:
        # Code to execute if value matches pattern1
    case pattern2:
        # Code to execute if value matches pattern2
    case _:
        # Default case (if no patterns match)
'''

# What is Match-Case?

# Match-case is a new feature introduced in Python 3.10 for pattern matching.

# It simplifies complex conditional logic.
