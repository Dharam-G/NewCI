def tempRange(temperature, isSummer):

	if (temperature > 59 and temperature < 90 and isSummer.lower() == "no"):
		limit = True
		print(limit, "- Temperature falls within the range.")
	
	elif (temperature > 59 and temperature < 101 and isSummer.lower() == "yes"):
		limit = True
		print(limit, "- Temperature falls within the range.")
	
	else:
		limit = False
		print(limit, "- Temperature does not fall within the range")
	
tempRange(int(input("What is the temperature? ")), str(input("Is it Summer? ")))