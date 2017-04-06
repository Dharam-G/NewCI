import math
import matplotlib.pyplot as plt

class Paint():
	def __init__(self):

		#cheapo data
		self.cheapoName = "CheapoMax"
		self.cheapoVolume = 20
		self.cheapoArea = 200
		self.cheapoPrice = 19.99
		self.cheapoPricePerArea = round((self.cheapoPrice/self.cheapoArea), 2)
		
		#AJ data
		self.AJName = "AverageJoes"
		self.AJVolume = 15
		self.AJArea = 165
		self.AJPrice = 17.99
		self.AJPricePerArea = round((self.AJPrice/self.AJArea), 2)
		
		#DP data
		self.DPName = "DuluxourousPaints"
		self.DPVolume = 10
		self.DPArea = 200
		self.DPPrice = 25
		self.DPPricePerArea = round((self.DPPrice/self.DPArea), 2)
		
		
class Calculations(Paint):

	def cheapestOverall():
	#Create instance of paint to access Paint class and create if statement to determine cheapest paint tin.
		a = Paint()
		
		if(a.cheapoPricePerArea < a.AJPricePerArea and a.cheapoPricePerArea < a.DPPricePerArea):
			print("CheapoMax has the lowest cost per area per tin with a value of £" + str(a.cheapoPricePerArea), "per square metre")
			
		elif(a.AJPricePerArea < a.cheapoPricePerArea and a.AJPricePerArea < a.DPPricePerArea):
			print("AverageJoes has the lowest cost per area per tin with a value of £" + str(a.AJPricePerArea), "per square metre")
			
		elif(a.DPPricePerArea < a.cheapoPricePerArea and a.DPPricePerArea < a.AJPricePerArea):
			print("DuluxourousPaints has the lowest cost per area per tin with a value of £" + str(a.DPPricePerArea), "per square metre")			
		
	def sizeOfRoom():
		
		global roomSize
	
	#User input for dimensions of room
		x = float(input("Enter width of room: "))
		y = float(input("Enter length of room: "))
		z = float(input("Enter height of room: "))
		
	#Calculate size of room and print as a round figure.
		roomSize = 2*x*z + 2*y*z + x*y
		res = round(roomSize, 2)
		print("Room size is", str(res), "square metres")
		return(roomSize)
		
		
	def priceForRoom():
		
		global noOfCheapoTins
		global noOfAJTins
		global noOfDPTins
		
	#Create instance of Paint class	
		b = Paint()
	
	#Calculate number of tins required to paint room for all three brands. Use math.ceil to round decimals up by 1
		noOfCheapoTins = math.ceil(roomSize/b.cheapoArea)
		noOfAJTins = math.ceil(roomSize/b.AJArea)
		noOfDPTins = math.ceil(roomSize/b.DPArea)
		
	#Calculate total price to paint the room for each brand
		cheapoTotalPrice = round((noOfCheapoTins * b.cheapoPrice), 2)
		AJTotalPrice = round((noOfAJTins * b.AJPrice), 2)
		DPTotalPrice = round((noOfDPTins * b.DPPrice), 2)
		
		cheapestPaintForRoom = None
		
	#If statement to determine which brand is cheapest to paint the room.	
		if (cheapoTotalPrice < AJTotalPrice and cheapoTotalPrice < DPTotalPrice):
			cheapestPaintForRoom = cheapoTotalPrice
			print(b.cheapoName, "costs the least to paint this room at £" + str(cheapoTotalPrice))
		
		elif (AJTotalPrice < cheapoTotalPrice and AJTotalPrice < DPTotalPrice):
			cheapestPaintForRoom = AJTotalPrice
			print(b.AJName, "costs the least to paint this room at £" + str(AJTotalPrice))
		
		elif (DPTotalPrice < cheapoTotalPrice and DPTotalPrice < AJTotalPrice):
			cheapestPaintForRoom = DPTotalPrice
			print(b.DPName, "costs the least to paint this room at £" + str(DPTotalPrice))

		return cheapestPaintForRoom
		
	def paintWaste():
	#Create instance of Paint class
		c = Paint()
		
	#calculate total area covered by tins bought
		cheapoTotalArea = noOfCheapoTins * c.cheapoArea
		AJTotalArea = noOfAJTins * c.AJArea
		DPTotalArea = noOfDPTins * c.DPArea

	#Calculate wastage in Area
		cheapoWasteArea = cheapoTotalArea - roomSize
		AJWasteArea = AJTotalArea - roomSize
		DPWasteArea = DPTotalArea - roomSize
		
	#Convert wastage to litres
		cheapoWasteLitres = round(c.cheapoVolume/cheapoWasteArea, 2)
		AJWasteLitres = round(c.AJVolume/AJWasteArea, 2)
		DPWasteLitres = round(c.DPVolume/DPWasteArea, 2)
		
	#If statement to find which brand(s) waste the least amount of paint.	
		if (cheapoWasteLitres < AJWasteLitres and cheapoWasteLitres < DPWasteLitres):
			print("CheapoMax wastes the least amount of paint. It wastes", str(cheapoWasteLitres) + "L")
			
		elif (AJWasteLitres < cheapoWasteLitres and AJWasteLitres < DPWasteLitres):
			print("AverageJoes wastes the least amount of paint. It wastes", str(AJWasteLitres) + "L")
			
		elif (DPWasteLitres < cheapoWasteLitres and DPWasteLitres < AJWasteLitres):
			print("DulucourousPaints wastes the least amount of paint. It wastes", str(DPWasteLitres) + "L")
			
		elif (cheapoWasteLitres == AJWasteLitres and cheapoWasteLitres == DPWasteLitres):
			print("All three brands waste the same amount of paint: ", str(cheapoWasteLitres) + "L")
			
		elif (cheapoWasteLitres == AJWasteLitres and cheapoWasteLitres < DPWasteLitres):
			print("CheapoMax and AverageJoes both waste the least amount of paint: ", str(cheapoWasteLitres) + "L")
			
		elif (cheapoWasteLitres == DPWasteLitres and cheapoWasteLitres < AJWasteLitres):
			print("CheapoMax and DuluxourousPaints both waste the least amount of paint: ", str(cheapoWasteLitres) + "L")
			
		elif (AJWasteLitres == DPWasteLitres and AJWasteLitres < cheapoWasteLitres):
			print("AverageJoes and DuluxourousPaints both waste the least amount of paint: ", str(AJWasteLitres) + "L")


	cheapestOverall()
	sizeOfRoom()
	priceForRoom()		
	paintWaste()
