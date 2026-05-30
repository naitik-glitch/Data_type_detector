def detect_type(data):
 
	try:
		int(data)
		print("Detected type : Integer")
	except:
				try:
					float(data)
					print("Detected type : Float")
				except:
					if data.lower() in ("true","false"):
						print("Detected type : Boolean")
					else:
						print("Detected type : String")
		
				
		 	
data = input("Enter Data type : ")
detect_type(data)


user_choice = input("Type 'Go' to continue : ")

while "go" in user_choice.lower():
			data = input("Enter Data type : ")
			detect_type(data)
			user_choice = input("Type 'Go' to continue : ")