#input phase
concerttickets = float(input("Enter Number of Concert Tickets: "))

#process phase
if concerttickets >= 25:
  priceperticket = 50
else:
 if concerttickets >= 10:
  priceperticket = 60
 else:
   if concerttickets >= 5:
     priceperticket = 70
   else:
     priceperticket = 75

total = concerttickets * priceperticket

#output phase 
print("Number of Tickets:", concerttickets)
print("Price per Ticket: $", priceperticket)
print("Total Cost: $", total)