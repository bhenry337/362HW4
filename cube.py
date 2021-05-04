def vol_cube(a):
	while True:
		try:
			b = int(a)
		except ValueError:
			print("Incorrect Input")
			quit()
		else:
			break
			
	if a < 0:
		print("Incorrect Input")
		quit()
		pass
	return a*a*a