# dictionary is denoted by flower brackets
cars = {"ferrari":"italy",
        "lamborghini":"italy",
        "fiat":"america",
        "tata":"india",
        "honda":"japan",
        "volkswagen":"germany"}

# you can also get the value of a key by using the below statement
print(cars["honda"])
# you can use .get function to find any key's value and if that key is absent then it gives result as none
print (cars.get("pagani"))
# you can also modify the result in get function as shown below
print(cars.get('pagani', 'car doesnt exist in database'))

# new function .split it splits by a space and stores it inside a list
new_car = input('enter_car_and_make: ').split()

# this is the way to append a new data into a dictionary
cars[new_car[0]]=new_car[1]

print(cars)
# you can also update the value of a key like this
cars["ferrari"] = "sri_lanka"

print(cars)

