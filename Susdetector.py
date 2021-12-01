#Made by Joshycosh
import random
import time
result = random.randint(0,100)
while True:
	print("**********")
	print("Start")
	print("Exit")
	print("**********")
	playerINPUT = input()
	if playerINPUT =="Exit":
		print("U seem kinda sus...")
		break
	elif playerINPUT =="Start":
		print("Starting sus detector..")
		time.sleep(3)
		for x in range (1,100):
			print("Calculating sussyness::", + x, "% COMPLETE")
			time.sleep(0.1)
		print("DETECTION FINISHED:")
		print("*****************************")
		result = print("You are ", + result, "% sus")
		print("****************************")
		break
		
