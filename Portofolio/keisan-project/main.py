# from otsuri import
# from stock import

goukei = float(input("Goukei ikura? "))
while True:
	haittaokane = float(input("Iretekudasai "))
	if haittaokane >= goukei:
		break
	else:
		print("Motto Iretekudasai")
otsuriokane(haittaokane,goukei)
