x = str(3)
y = int(4)
z = float(3)
print(type(x))

print("capitalize() function")
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

print("casefold() function")
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

print("center() function")
txt = "banana"
x = txt.center(20)
print(x)

print("count() function")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

print("encode() function")
txt = "My name is Ståle Trường"
x = txt.encode()
print(x)

print("\nendswith() function")
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

print("\nexpandtabs() function")
txt = "H\te\tl\tl\to"
x = txt.expandtabs(3)
print(x)

print("\nfind() function")
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

print("\nformat() function")
txt = "For only {price:.2f} dollars!"
print( txt.format(price = 49))
print("My name is {fname}, I'm {age}".format(fname = "John", age = 36))
print("My name is {0}, I'm {1}".format("John", 36))
print("My name is {}, I'm {}".format("John", 36) )
i = 0
print("\nformat :< ")
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters
# Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print( txt.format(49))
# Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))
# Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))
# Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
# Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
# Use "-" to always indicate if the number is negative (positive numbrs are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3,7))
# Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3,7))
# Use "," to add a comma as a thousand separator:
print("The universe is {:,} years old.".format(13800000000))
# Use "_" to add a underscore character as a thousand separator:
print("The universe is {:_} years old.".format(13800000000))
#Use "b" to convert the number into binary format:
print("The binary version of {0} is {0:b}".format(5))
#Use "d" to convert a number, in this case a binary number, into decimal number format:
print("We have {:d} chickets.".format(0b101))
#Use "e" to convert a number into scientific number format (with a lower-case e):
print("We have {:e} chickens.".format(5))
#Use "E" to convert a number into scientific number format (with an upper-case E):
print("We have {:E} chickens.".format(5))
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
print("The price is {:.2f} dollars.".format(45))
#without the ".2" inside the placeholder, this number will be displayed like this:
print("The price is {:f} dollars.".format(45))
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
print("The price is {:F} dollars.".format(x))
#same example, but with a lower case f:
print("The price is {:f} dollars.".format(x))
#Use "o" to convert the number into octal format:
print("The octal version of {0} is {0:o}".format(10))
#Use "x" to convert the number into Hex format:
print(f"The Hexadecimal version of {255} is {255:x}")
#Use "X" to convert the number into upper-case Hex format:
print(f"The Hexadecimal version of {255} is {255:X}")
#Use "%" to convert the number into a percentage format:
print(f"You scored {0.25:%}")
#Or, without any decimals:
print(f"You scored {0.25:.0%}")

print("Hello, welcome to my world.".index("welcome"))
print("Hello, welcome to my world.".index("e", 5, 10))
print("Hello, welcom to my world.".find("welcome"))
try:
    print("Hello, welcom to my world.".index("welcome"))
except:
    print("can't find")
print("isalnum()", "Company12".isalnum())
print("Company 12".isalnum())
print("isalpha()", "CompanyX".isalpha())
print("Company10".isalpha())
print("isascii()", "Company123".isascii())
print("isdecimal()", "1234".isdecimal())
print("\u0030".isdecimal()) # unicode for 0
print("\u0047".isdecimal()) # unicode for G
print("isdigit()", "50800".isdigit())
print("\u0030".isdigit()) # unicode for 0
print("\u00B2".isdigit()) # unicode for sup 2
print("'Demo'.isidentifier()", "Demo".isidentifier())
print("'hello world!'.islower()", 'hello world!'.islower())
print("'Hello World!'.islower()", 'Hello World!'.islower())
print("'hello world 123!'.islower()", 'hello world 123!'.islower())
print("isnumeric()", "565543".isnumeric())
print("isnumeric()", "\u0030".isnumeric())
print("isnumeric()", "\u00b2".isnumeric())
print("isnumeric()", "10km2".isnumeric())
print("isnumeric()", "-1".isnumeric())
print("'1.5'isnumeric()", '1.5'.isnumeric())
print("'Hello! Are you #1?'.isprintable()", 'Hello! Are you #1?'.isprintable())
print("'Hello! \nAre you #1?'.isprintable()", 'Hello! \nAre you #1?'.isprintable())
print("'  '.isspace()", '  '.isspace())
print("' a '.isspace()", ' a '.isspace())
print("'Hello, And Welcome To My World!'.istitle() #", 'Hello, And Welcome To My World!'.istitle())
print("'HELLO, AND WELCOME TO MY WORLD!'.istitle() #", 'HELLO, AND WELCOME TO MY WORLD!'.istitle())
print("'22 Names'.istitle() #", '22 Names'.istitle())
print("'This Is %\'!'.istitle() #", 'This Is %\'!'.istitle())
print("'THIS IS NOW!'.isupper()", 'THIS IS NOW!'.isupper())
print('Hello World!'.isupper())
print('hello 123!'.isupper())
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
