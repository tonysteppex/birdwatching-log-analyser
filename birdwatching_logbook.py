birds = ["Kingfisher", "Sparrow", "Eagle", "Parrot", "Owl"]

while True:
    bird = input("\nWhat bird did you observe today? ").strip()

    if bird:
        birds.append(bird)
        print(f"\nBirds: {birds}")
        print(f"Number of birds observed: {len(birds)}")
    else:
        print("\nError: No bird name entered. Please try again.")
        continue

    while True:
        continue_logging = input(
            "\nWould you like to log another bird? (yes/no): "
        ).strip().lower()

        if continue_logging == "yes":
            break
        elif continue_logging == "no":
            print("\nExiting Birdwatching Logbook...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if continue_logging == "no":
        break

print("\nFinal Birdwatching Logbook:")
for bird in birds:
    print(f"- {bird}")

print(f"\nTotal birds recorded: {len(birds)}")