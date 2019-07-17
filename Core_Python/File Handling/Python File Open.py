# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

path: str = "C:/Users/Misran Rifat/PycharmProjects/Python-Practice/demofile.txt"

f = open(path, "r")
print(f.read())

print('================================')

f = open(path, "r")
# Return the 5 first characters of the file:
print(f.read(5))

print('================================')

# Read Lines

f = open(path, "r")
print(f.readline())

print('================================')

# By calling readline() two times, you can read the two first lines:
f = open(path, "r")
print(f.readline())
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:
print('================================')

f = open(path, "r")
for x in f:
    print(x)

print('================================')
# Close Files
f = open(path, "r")
print(f.readline())
print('Closing a file =================')
f.close()
