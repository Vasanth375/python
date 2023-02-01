def nearly_equal(a, b):
    if a == b:
        return True
    return False

# Example usage:
string1 = "hello"
string2 = "Hello"

if nearly_equal(string1, string2):
    print("The strings are nearly equal.")
else:
    print("The strings are not nearly equal.")
