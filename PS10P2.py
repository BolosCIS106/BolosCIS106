def square_footage(length, width, height):
  area = 2 * length * width
  wall1 = 2 * length * height
  wall2 = 2 * width * height
  total = area + wall1 + wall2
  return total

def calculate_paint(square_footage):
  gallons = square_footage / 50
  return gallons

while True:
  r = input("Do you want to calculate gallons of paint for a room?: (Yes or No)")
  if r == "Yes":
    length = float(input("Enter the length of the room: "))
    width = float(input("Enter the width of the room: "))
    height = float(input("Enter the height of the room: "))
    square_footage = square_footage(length, width, height)
    gallons = calculate_paint(square_footage)
    print(f"\nFor the room with dimensions {length}x{width}x{height} feet: ")
    print(f"square footage: {square_footage} square feet")
    print(f"gallons_needed: {gallons: .2f} gallons\n")