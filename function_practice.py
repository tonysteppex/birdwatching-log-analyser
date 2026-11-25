def record_bird(bird):
    print(f"Bird recorded: {bird}")
    return bird

sparrow = record_bird("Sparrow")
robin = record_bird("Robin")
parrot = record_bird("Parrot")

print("\nReturned values:")
print(sparrow)
print(robin)
print(parrot)