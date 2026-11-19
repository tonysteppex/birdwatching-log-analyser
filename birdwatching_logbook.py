bird = input("What bird did you observe today? ").strip()
location = input("Where did you observe the bird? ").strip()
date = input("What date did you observe the bird? ").strip()

if bird and location and date:
    print("=" * 30)
    print(f"{'SIGHTING RECORDED':^30}")
    print("=" * 30)

    print(f"Bird: {bird}")
    print(f"Location: {location}")
    print(f"Date: {date}")

    print("\nThank you for using the Birdwatching Logbook!")

else:
    print("\nERROR: Please provide all the required information (bird, location, and date).")
    if not bird:
        print("Bird name is missing.")
    if not location:
        print("Location is missing.")
    if not date:
        print("Date is missing.")
