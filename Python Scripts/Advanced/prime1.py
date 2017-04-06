import time
import math

def primeNumbers():

	start_time = time.time()

	for i in range(1000001, 3000001, 2):
#Following line not needed to stay in time limit but does decrease time
		if (i%3!=0 and i%5!=0 and i%7!=0 and i%9!=0 and i%11!=0 and i%13!=0 and i%17!=0 and i%19!=0 and i%23!=0 and i%29!=0):
			if all(i%j!=0 for j in range (1000000, int(math.sqrt(i))+1)):
				print(i)

	print("--- %s seconds ---" % (time.time() - start_time))

primeNumbers()