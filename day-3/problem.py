#givem a list of tuples wiith info(name,subject);
#list all unique course
#list students enrolled in english
#create dictionary (student,set of courses)


students = [
    ("monu","english"),
    ("vikas","hindi"),
    ("pal","maths"),
    ("om","science"),
    ("ram","english"),
    ("shyam","maths"),
    ("ajay","hindi"),
    ("aksay","science"),
    ("vijay","english"),
    ("anjit","maths"),
    ("aman","hindi"),               
    ("ankit","english")
]
#list all unique course

# unique_courses = set()
# for student in students:
#     unique_courses.add(student[1])
# print(unique_courses)

#1
unique_course =set()

for tup in students:
    print(tup[1])
    unique_course.add(tup[1])
    
print(unique_course)

#2
students_in_english =[]
no_std_in_english =0
for name , course in students:
    if course == "english":
        no_std_in_english += 1
        students_in_english.append(name)
print(f"{no_std_in_english} students enrolled in english are {students_in_english}")

#3

dict={}
for name, course in students:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
        
print(dict)