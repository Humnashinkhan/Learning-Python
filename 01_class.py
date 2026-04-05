class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


harry = Employee()
harry.name = "Harry" # This is an instance attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)