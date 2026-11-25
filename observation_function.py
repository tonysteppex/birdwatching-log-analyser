def record_bird(bird, location, date, weather, time):

    sighting = {
        "bird": bird,
        "location": location,
        "date": date,
        "weather": weather,
        "time": time
    }

    return sighting

sighting = record_bird(
    "Kingfisher",
    "Jabi Lake",
    "25-11-2026",
    "Sunny",
    "10:30 AM"
)

print(sighting)