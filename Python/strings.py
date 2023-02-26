# CREATE A VARIABLE
# text data is called string
message = "Hello world"
print(message)

# multi line text
new_message = """This is a multi line string
my name is balaji
How are you?
"""
print(new_message)
print("The length of the message -message- : {}".format(len(message)))
print("Printing the starting letter of new_message : {}".format(new_message[0]))
print("Python slicing... Printing world : {}".format(message[6:]))

capitalize_custom = "HskdiEKasKJDJKASCksdlajsdSILJD"
my_name = "BALAJI"
print("Converting it to lower case : {}".format(capitalize_custom.lower()))
print("Converting it to upper case : {}".format(capitalize_custom.upper()))
print("Checking whether my_name is all caps : {}".format(my_name.isupper()))

print(f"Swapping case for capitalize_custom {capitalize_custom.swapcase()}")
# print(dir(capitalize_custom))
# printing the index of l in message ***ALL INDEXES***
index_l = [i+1 for i, letter in enumerate(message) if letter == "l"]
print(index_l)

lstrip_message = "..;/;,,balaji bharatwaj..;/;,,"
print(lstrip_message.strip(".;/,"))