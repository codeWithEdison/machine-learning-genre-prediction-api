# variable 
name = "john doe"
age = 10
is_student= True

# basic operations
sum = 10  + 5

# control structure


if age >= 18 :
    print( "is an adult")
elif age > 13:
    print("is a teenager")
else:
    print("is a child")
    
## loop
# for i in range(10):
#     print('*')
    
# while age< 30:
#  age += 1
#  print(age)

for i in range(5):
    for j in range(i+1):
        print('*', end= "")
    print()
    
#list 
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# dictionary

person = {
    "name": "John Doe",
    "age": 30,
    "is_student": True
}

print(person["name"])

# Sets

numbers = {1, 2, 3, 4, 5, 1,3,4}
for number in numbers:
    print(number)

# Tuples

coordinates = (10, 20)
print(coordinates[0])

# functions
def greet(name, age):
    print(f"Hello, {name}  with {age} years !") 
    
greet('john', 20)
# special purpose function
# print(sorted[3,2,5,1,6])

# lambda

multiply = lambda x, y: x * y
print(multiply(3, 5))

# geneartor
# Normal function returns all values at once
def get_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers

# Generator gives one value at a time
def get_numbers_generator(n):
    for i in range(n):
        yield i

# See the difference
regular = get_numbers(3)      # Creates [0,1,2] immediately
generator = get_numbers_generator(3)  # Creates values as needed
print(next(generator))  # 0
print(next(generator))  # 1

# oop

class Dog:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print(f"{self.name} is barking!")
        
dog = Dog("Buddy")

dog.bark()