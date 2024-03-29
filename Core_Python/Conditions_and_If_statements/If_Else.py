# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
c = 55

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

if a > b: print("a is greater than b")

print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

if b < a < c:
    print("Both conditions are True")

if a > b or a > c:
    print("At least one of the conditions is True")
