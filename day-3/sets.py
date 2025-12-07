#set 

s={23,34,45,56,67,78,89,90}

empty_set = set()
print(type(empty_set))

print(s)
print(type(s))

print("Length of set is ", len(s))
s.add(100) #adding element
print(s)
s.remove(34) #removes specific element, raises error if not found
print(s)
s.discard(200)  
print(s)
s.pop() #removes an arbitrary element
print("dffffff",s)
s.clear() #removes all elements
print(s)    

