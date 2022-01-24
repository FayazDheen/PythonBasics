person={"name":"John","gender":"male","age":25,"address":"empty street","phone":"+919876543210"}
property = input("What Info you want to know about the person? ").lower()
print(person.get(property,"That info is not available right now!!" ))  
