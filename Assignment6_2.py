# Create a function to reverse a string
def reverse_string(string):
    # Base case: if the string is empty or it has one character
    if len(string) <= 1:
        return string

    # Recursive case: Reverse and append
    else:
         return reverse_string(string[1:]) + string[0]


    print(reverse_string("hello"))
    

