# Function to check the validity of file
def read_file(filename):
# Try opening the file
try:
# Open the file in read mode
f = open(filename, "r")
return f
# Raise exception in other case
except:
print(f"Error -- There is an issue with file {filename}. Please reenter:")
# main function
if __name__ == '__main__':
# Dictionary to store the data of the file
fooditems = {}
# Endless loop runs until the correct file name is given
while(True):
# Get the filename
filename = input("Enter the input file name: ")
filee = read_file(filename)
# if the filehandle is returned
if(filee):
# Read the contents of the file and read the food_name and price
# and then store them in the Dictionary
for i in filee.read().splitlines():
# strip removes extra whitespace characters
foodname = i[:16].strip()
price = float(i[16:])
fooditems[foodname] = price
# after reading the file, break the loop
break
else:
continue
# Print the output report
print("Output Report:"+'-'*25+"\n")
print("The total number of items sold is: ",len(fooditems))
# declare variables
pizza = 0
burger = 0
total = 0
# It returns a sorted list of items
d = sorted(fooditems)
# For each item in the list, check if pizza or burger is present or not
for i in d:
if('pizza' in i.lower()):
pizza += 1
elif('burger' in i.lower()):
burger += 1
# add the total price
total += fooditems[i]
# Print the total number of pizza and burger
print(f"Total number of items with pizza is: {pizza}")
print(f"Total number of items with burger is: {burger}")
print("{:<20}{:<11}".format("Food Item", "Amount Sold"))
print("{:<20}{:<11}".format("---------", "-----------"))
# Print the dictioanry in sorted order
for i in d:
print("{:<20}${:.2f}".format(i,fooditems[i]))
# print the sub_total
print("\nThe sub total sold is: ${:.2f}".format(total))
# calculate the tax
tax = total * 0.06
print("The total tax is: ${:.2f}".format(tax))
# Print grand total
print("\nThe grand total collected for the night is: $
{:.2f}".format(total+tax))
