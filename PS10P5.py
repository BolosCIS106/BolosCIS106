def compute_value(county, market_value):
  assessed_percentages = {
      'Cook': 0.90,
      'DuPage': 0.80,
      'McHenry': 0.75,
      'Kane': 0.60,
      'All others': 0.70,
  }

  value_percent = assessed_percentages.get(county, 0.70)
  assessed_value = market_value * value_percent
  return assessed_value

total_market_value = 0
total_assessed_value = 0

while True:
  r = input("Do you want to run this program? (Yes or No): ").strip().lower()

  if r != 'yes':
      break

  county = input("Enter the county of the home: ")
  market_value = float(input("Enter the market value of the home: "))

  assessed_value = compute_value(county, market_value)

  print(f"\nFor a home in {county} with a market value of ${market_value}:")
  print(f"Assessed Value: ${assessed_value}\n")


  total_market_value = market_value
  total_assessed_value = assessed_value