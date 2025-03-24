a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print('Number 1:', a)
print('Number 2:', b)

Add = a + b
sub = a - b
mul = a * b
div = a / b
rem = a % b

print('Addition:', Add)
print('Subtraction:', sub)
print('Multiplication:', mul)
print('Division:', div)
print('Remainder:', rem)

if Add % 2 == 0 and sub % 2 == 0 and mul % 2 == 0 and div % 2 == 0 and rem % 2 == 0:
    print('All results are even.')
else:
    print('At least one result is odd.')
