user = int(input("Enter the size of the pattern: "))# user input
i = 0
while i < user:
    for j in range(user):
        print("*", end="")
    print()  # Print a newline character after each row
    i += 1
