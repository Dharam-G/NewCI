class computerStatus():

	def __init__(self, power):
		self.power = power
		
	def bootPC(self):
		for line in self.power:
			print(line)
			
turn_power_on = computerStatus(["Compuetr is turning on"])


turn_power_on.bootPC()