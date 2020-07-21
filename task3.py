NUM = int(input("Enter NUM: "))
n = int(input("Enter number: "))
if NUM >= -3 and NUM <= 20:
    if n == NUM:
        print("Success!")
    if n > NUM:
        print("More than")
    if n < NUM:
        print("Less than")
else:
    print("Try again")
