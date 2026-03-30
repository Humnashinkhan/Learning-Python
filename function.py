#  there is no input no output
def greet():
    print("Hello")

greet()        

# Function with Parameters & without Return
def greet(name):
    print("Hello", name)

greet("Ravi")

# Function without Parameters & with Return

def get_num():
    return 10

print(get_num())

# Function with Parameters & with Return ✅ (Most Important)

def add(a, b):
    return a + b

print(add(2, 3))