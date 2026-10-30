
# Check palindrome string

string = input("Enter a string: ")

reverse = string[::-1]

if string.lower() == reverse.lower():
    print("Given string is Palindrome")
else:
    print("Given string is Not Palindrome")