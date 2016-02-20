import sys

word = "Welcome to the supermarket!"
print "\n"* 5
print word.upper()
print "\n"* 5
print "use q as an input for any question to leave the program"
		
stock = {"orange": 15, "apple": 20, "pear": 14, "cigarettes": 18}

price = {"orange": 2.50, "apple": 2.65, "pear": 2.80, "cigarettes": 100}

for index, x in enumerate(price, start=1):
	print index, str(x)
	print "Cost: $%r." % price[x]
	print "We have %r in stock." %stock[x]
	print "\n"*1
	


def run():
	list = {}
	loop_condition = True
	while loop_condition:	#Asking the user what they want.
		try:
			items = raw_input("Enter what you'd like to buy >").split(", ")
			print "\n"*1
			if items[0] == "q":
				return
			for i in items:
				if i in stock:
					print "Item ", i, " has ", stock[i], "available."
					print "\n"*1
					for x in items:
						list[x] = 0 
					loop_condition = False

				else:
					print "No items of ", i, " available, did you spell that correctly?"
		except TypeError:
			print "Looks like you've entered an invalid format."		
			continue

	print list
	print "\n"*1
	print "Great!, now for the quantity!"

	loop_condition2 = True
	
	while loop_condition2:
		for y in list:
			num = raw_input("How many/much %s do you want?") %y
			y[num]
			print list
			
			loop_condition2= False	
if __name__ == "__main__":
	run()
	

			
	