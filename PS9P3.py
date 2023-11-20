def calculate_mpg(miles, gallons):
    """Calculate miles per gallon."""
    if gallons != 0:
        return miles / gallons
    else:
        return 0

entries = 0

while True:
    try:
        destinationcity = input("Enter the destination city: ")
        milestraveled = float(input("Enter miles traveled: "))
        gallonsused = float(input("Enter gallons used: "))

        mpg = calculate_mpg(milestraveled, gallonsused)

        print(f"\nTrip {entries + 1} Details:")
        print(f"Destination City: {destinationcity}")
        print(f"Miles Traveled: {milestraveled} miles")
        print(f"MPG: {mpg:.2f} miles per gallon\n")

        entries += 1

    except (EOFError, KeyboardInterrupt):
        break

print("nNumber of Entries Made:", entries)