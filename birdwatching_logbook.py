sightings = []

print("==============================")
print("     BIRDWATCHING LOGBOOK")
print("==============================")

while True:
    bird = input("\nBirdname: ").strip()
    location = input("Observation location: ").strip()
    date = input("Observation date (YYYY-MM-DD): ").strip()
    weather = input("Weather: ").strip()
    time = input("Observation time: ").strip()

    if bird and location and date:
        sighting = {
            "bird": bird,
            "location": location,
            "date": date,
            "weather": weather,
            "time": time
        }

        sightings.append(sighting)

        print("\nObservation successfully recorded!")
    else:
        print("\nError: Bird name, location, and date are required.")

    while True:
        answer = input("\nDo you want to add another observation? (yes/no): ").strip().lower()

        if answer == "yes":
            break
        elif answer == "no":
            break
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

    if answer == "no":
        break

print("\n========== YOUR OBSERVATIONS ==========")

for sighting in sightings:
    print("------------------------------")
    print(f"Bird: {sighting['bird']}")
    print(f"Location: {sighting['location']}")
    print(f"Date: {sighting['date']}")
    print(f"Weather: {sighting['weather']}")
    print(f"Time: {sighting['time']}")

print("------------------------------")
print(f"Total observations recorded: {len(sightings)}")
print("Thank you for using the Birdwatching Logbook!")
