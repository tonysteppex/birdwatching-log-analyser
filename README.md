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