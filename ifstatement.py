num = int(input("Enter the Number : "))
num2 = int(input("Enter the Number to check odd or even : "))

if num > 0:
    print(f"The { num} is positive number")
elif num == 0:
    print(f"The {num} is zero")

else:
    print(f"The {num} is negative")


if num2 % 2 == 0:
    print(f"the {num2} is even")
else:
    print(f"the {num2} is odd number")
