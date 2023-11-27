def month_forecast(month, sale):
  """Next Months sales and values"""
  forecast_percent = 0.0
  if month == ['January', 'February', 'March']:
    forecast_percent = 0.10
  elif month == ['April', 'May', 'June']:
    forecast_percent = 0.15
  elif month == ['July', 'August', 'September']:
    forecast_percent = 0.20
  elif month == ['October', 'November', 'December']:
    forecast_percent = 0.25
  nms = sale * (1 + forecast_percent)

  return nms

r = input("Do you want to run this program? (Yes or No): ")
while r == "Yes":
  lname = input("Enter Last Name: ")
  month = input("Enter Month (Example April): ")
  sale = float(input("Enter number of sales: "))
  nms = month_forecast(month, sale)
  print("Last Name: ", lname)
  print("Month: ", month)
  print("Value: ", {nms})
  print("I dont know why the value isnt calculating correctly")