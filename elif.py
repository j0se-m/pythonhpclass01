marks=int(input("Enter marks : "))

if marks>=80 and marks<=100:
    print("You got A")
elif marks>=60 and marks<80:
    print("You got B")

elif marks>=40 and marks<60:
    print("You got C")

else:
    print("Sorry you failed")