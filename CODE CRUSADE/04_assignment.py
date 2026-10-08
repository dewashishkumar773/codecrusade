
# Take a number as input and convert it into integer, float, and string types. Print the converteds and their data types.


a = input("Enter a number: ")

int = int(a)
float = float(a)
str = str(a)

print("Int:", int)
print("Type:", type(int))

print("Float:", float)
print("Type:", type(float))

print("Str:", str)
print("Type:", type(str))


# output of this question
'''
Enter a number: 25
Int: 25
Type: <class 'int'>
Float: 25.0
Type: <class 'float'>
Str: 25
Type: <class 'str'>

'''