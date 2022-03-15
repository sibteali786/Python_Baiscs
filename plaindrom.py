
############################# Checking if a string is palindrome or not  ############################



def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for i in input_string:
        if ~i.isspace():
            new_string = new_string.strip() + i.lower()
            reverse_string = i.lower() + reverse_string.strip()

    print(reverse_string)
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False



print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
# is_palindrome("kayak")
