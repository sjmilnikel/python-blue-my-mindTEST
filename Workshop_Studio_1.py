user = {"first_name" : "Ada"}
print(user["first_name"])

user["family_name"] = "Byron"
print(user)

user["family_name"] = "Lovelace"
print(user)

del user["family_name"]
print(user)

fruit = ["apples","oranges","bananas"]
print(len(fruit))

print(fruit[-2])

fruit.append("kiwi")
print(fruit)

fruit.insert(2, "passion fruit")
print(fruit)

print(sorted(fruit))

print(fruit)

fruit.sort()
print(fruit)

fruit.reverse()
print(fruit)

del fruit[1]
print(fruit)

favorite_fruit = fruit.pop()
print(favorite_fruit)

fresh_fruit = fruit.pop(1)
print(fresh_fruit)

fruit.remove('bananas')
print(fruit)

my_variable = "A string"
print(type(my_variable))

my_number = 50
some_string = "The number is "
print(some_string + str(my_number))

