def calculate_batting_average(hits, at_bats):
    return hits / at_bats if at_bats != 0 else 0.0

players_count = 0

while True:
    try:
        last_name = input("Enter player's last name: ")
        hits = float(input("Enter number of hits: "))
        at_bats = float(input("Enter number of at bats: "))

        average = calculate_batting_average(hits, at_bats)

        print(f"{last_name}'s batting average: {average:.3f}")
        players_count += 1

    except (EOFError, KeyboardInterrupt):
        break

print(f"\nNumber of players entered: {players_count}")