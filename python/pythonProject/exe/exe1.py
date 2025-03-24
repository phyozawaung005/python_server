#num: int
#for num in range(-10, 0, 2):

num: int = int(input('Enter your num:'))

total = 0
for num in range(1, num + 1):
    total += num
    # print(n)
print(total)