def compute_ticket(miles):
    if miles >= 30:
        return 12
    elif 20 <= miles <= 29:
        return 10
    elif 10 <= miles <= 19:
        return 8
    else:
        return 5

total = 0

while input("Calculate train ticket price? (Yes or No): ").strip().lower() == 'yes':
    lname = input("Last Name: ")
    miles = int(input("Enter the miles: "))

    ticket_price = compute_ticket(miles)

    print(f"\nFor Mr. {lname},Took {miles} miles from downtown Chicago:")
    print(f"Train Ticket Price: ${ticket_price}")

    total += ticket_price

print(f"\nSum of all Train Ticket Prices: ${total}")