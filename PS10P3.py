def compute_out_the_door_price(msrp, make, model, code):
  discounts = {
      ('Honda', 'Accord'): 0.10,
      ('Toyota', 'Rav4'): 0.15,
      ('', '', 'Y'): 0.30,  
  }

  percent_off = discounts.get((make, model, code), 0.05)
  new_msrp = msrp * (1 - percent_off)
  total_price = new_msrp * 1.07

  return total_price, new_msrp

total_msrp = 0
total_sales_price = 0

while True:
  r = input("Do you want to enter information for an automobile? (Yes or No): ")

  if r != 'Yes':
      break

  make = input("Enter the make of the automobile: ")
  model = input("Enter the model of the automobile: ")
  code = input("Is it an electric vehicle? (Y/N): ").strip().upper()
  msrp = float(input("Enter the MSRP (sticker price) of the automobile: "))

  total_price, new_msrp = compute_out_the_door_price(msrp, make, model, code)

  print(f"\nFor the {make} {model} with MSRP ${msrp:.2f}:")
  print(f"Discounted MSRP: ${new_msrp:.2f}")
  print(f"Total Out-the-Door Price: ${total_price:.2f}\n")


  total_msrp += msrp
  total_sales_price += total_price

print(f"\nSum of all MSRP's: ${total_msrp:.2f}")
print(f"Sum of all Sales Prices: ${total_sales_price:.2f}")