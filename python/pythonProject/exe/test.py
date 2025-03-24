

while True:
    a = int(input('Input Number1= '))
    print("First Number that you input=", a)
    b = int(input('Input Number2= '))
    print("Second Number that you input=", b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

    choice = input("Do you want to calculate again? (yes/no): ")
    if choice.lower() != "yes":
        print("Process finished.")
        break
