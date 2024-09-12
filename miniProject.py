print("Welcome to the space travel calculator.")
distance = int(input("How many light years away is your destination?"))
speed = int(input("Hoe fast is your spaceship?"))
time = distance / speed
print(
    "It will take you", time, "light years to get there."
) 