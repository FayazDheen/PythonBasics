List []  
Tuples ()  
List are Mutable  
Tuples are immutable  

students = ["John","Mary","Steve"]  
add elemnt to last of list we can use append()  
student.append("Kate")  

To add an item specifically to position use insert() which take 2 arguemnts insert(position,data)  
student.insert(0,"Bishop")  

To remove item pop() which return last item    
To remove specific item pass postion to pop() => student.pop(2)  

To remove specific item we can use remove()  
student.remove("Mary")  Be cautious with remove, case sensitive  

merge 2 list with + operator  
we can also merge 2 tuples  
But not merge List with tuple  
