# Python 3 program to check if a given string
# is a valid integer

# This function returns True if s is a number else False
def isNumber(s):
    for char in s:
        if not char.isdigit():
            return False
    return True

# Driver code
if __name__ == "__main__":
    # Store the input in a variable named 'str_input' (avoid using 'str' as it's a built-in type)
    str_input = "6790"

    # Function Call
    if isNumber(str_input):
        print("Integer")
    else:
        print("String")
