string_value = input("Enter the string: ")
integer_value = int(string_value)
back_to_string = str(integer_value)

print(f"The string: {string_value} is {type(string_value)} ")
print(f"The converted  interger value: {integer_value} is {type(integer_value)} ")
print(f"Back to string value: {back_to_string} is {type(back_to_string)} ")