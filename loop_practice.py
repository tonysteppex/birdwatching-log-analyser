name = input("Enter your name: ")
print(f"Hello, {name}!")

answer = "yes"

while answer != "no":
    answer = input("Do you want to continue? (yes/maybe/no): ").lower()
    if answer == "yes":
        print("Continuing...")
    elif answer == "maybe":
        print("Maybe later...")
    elif answer == "no":
        print("Exiting...")
    else:
        print("Invalid input. Please enter 'yes', 'maybe', or 'no'.")