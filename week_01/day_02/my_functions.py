def greet(name):
    return "Hey " + name

greeting = greet("bob")

print(greeting)

def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name

greeting = greet('Bob', 'Morning')

print(greeting)