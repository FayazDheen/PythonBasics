month = ("January","February", "March" ,"April","May","June","July", "August", "September", "October", "November", "December")
birthday = input("Enter birthday in format DD-MM-YYYY: ")
index = int(birthday[3:5]) -1
bd_month = month[index]
print("Your born in",bd_month)                 
