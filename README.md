BIRDWATCHING LOGBOOK v0.1
01 RECORD A BIRD SIGHTING
the program should ask three questions:
a. what bird did you observe?
b. where did you see it?
c. when did you see it?

Attempt:
bird = input("What bird did you observe today? ")
print(f"You observed a {bird}!")

location = input("Where did you observe the bird? ")
print(f"You observed the {bird} at {location}.")

date = input("What date did you observe the bird? ")
print(f"You observed the {bird} at {location} on {date}.")

Better presentation attempt:
.strip() removes accidental spaces at the beginning and end of an answer. For example, entering three spaces won't count as meaningful information.

don't need str() around your text or f-strings. print() already knows how to display them.

if/else Allows your program to make decisions.

^ means centre the text.
30 means use a total width of 30 characters.

Nested conditions: You can put an if statement inside an else block.

Next feature: v0.2
Think about birdwatching observations. Instead of displaying one bird and losing the information when the program ends, i want to keep several observations together.
List :birds = ["Pied Crow", "Village Weaver", "Common Bulbul"]
The application should continue accepting observations when the answer is yes and stop when the answer is no.

Three Python concepts will make this possible:
a. while loop: Allows users to keep entering sightings.
b. Lists: Hold multiple sightings together.
c. Dictionaries: Store each sighting's bird, location and date as related information.

lower(). It converts the answer to lowercase, so YES, Yes and yes are treated consistently.

len() that counts how many items are in a list.
.append() that adds an item to an existing list.
break: Stops the loop when requested.
Dictionaries to store each observation as a complete record.
Key identifies the information, while the value contains the actual information.
sightings = [] Creates an empty list
while True: Keeps the application running
{...}: Creates an observation dictionary
for sighting in sightings: Goes through every observation.
len(sightings): Counts the observations.

####Saving observations with JSON (JavaScript Object Notation)
##Persistent data storage
1. open(): Opens or creates a file
2. "w": Opens the file for writing, replacing its previous contents.
3. encoding="utf-8": Supports a wide range of characters
4. with: Manages the file and closes it automatically
5. json.dump(): Converts and writes Python data into JSON
6. indent=4: Makes the JSON easier to read
7. "r" means read mode.
8. json.load() converts the JSON information back into Python lists and dictionaries.
9. Why the try and except?
The first time you run the program, sightings.json won't exist. Python would normally produce a FileNotFoundError.
We use except to handle that situation and start with an empty list instead.
10. .get() allows you to provide a default value when a key doesn't exist.
