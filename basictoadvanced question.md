1. What is Python?

   Python is a popular, high-level, programming language used for building web applications, data analysis, AI, and automation.

2. What are Data Types?

   Data types define what kind of value a variable holds.
   Common data types in Python:

    int → numbers → 10
    foat → decimal → 10.5
    str → text → "hello"
    bool → True/False
    list → [1, 2, 3]
    tuple → (1, 2, 3)
    dict → {"a":1}

3. Difference between List vs Tuple
   
   A list is a collection of items stored in a single variable, and it can be changed (mutable). list use square brackets []. slower 

   A tuple is also a collection of items, but it cannot be changed (immutable).
   tuple use paranthesis (). faster 

4. What is a Dictionary?
   
   Dictionary stores data in key-value pairs. and it is used to quickly access values.
   eg. 
       student = {
       "name": "Ravi",
       "age": 21
     }

     print(student["name"])

5. What is a Variable?
   
   “Variable is a container that stores data which can be used later in the program.”

6. Difference between return vs print
   
   print() → shows output on screen
   return → sends value back from function, so it can be used later.

7. What is Lambda Function?
   
   A lambda function is a small anonymous function written in one line.
   without a name, used for short operations.

8. What are *args and **kwargs?

   args (Non-keyword arguments): args is used to pass multiple values to a function

    def add(*numbers):
    print(sum(numbers))

    add(1, 2, 3, 4)
 
 kwargs (Keyword arguments): kwargs is used to pass multiple key-value arguments.

 def info(**data):
    print(data)

 info(name="Ravi", age=21)
 