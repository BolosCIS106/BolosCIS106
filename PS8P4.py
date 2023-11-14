f = open("data4.txt", "r")

#initalize counters and sums to 0
c = 0.0
tot_ep = 0.0

#get first data line
item = str(f.readline().rstrip('\n'))

while item != "":
    qty = float(f.readline())
  price = float(f.readline())
ep = qty * price
tot_ep = tot_ep + ep
c = c + 1

#display a line of data
print("Item is:    ", item)
print("Quantity is:    ", qty)
print("Price is:    ", price)
print("Extended price:    ", ep)

#get next data 
item = str(f.readline().rstrip('\n'))

#after the loop
#final calculations
#display them and sums and counts
print("Total Extended Prices: ", tot_ep)
print("Number of Orderes: ", c)
avg = tot_ep / c
print("Average Order:    ", avg)