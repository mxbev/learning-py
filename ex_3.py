bicycles = ['trek', 'cannondale', 'cervelo', 'specialized']
print(bicycles)

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# 3-1
names = ['james', 'tom', 'freya', 'sam', 'abi']
print(names[-1])
print(names[4])

# 3-2
message = f"Hello {names[4].title()}, how are you?"
print(message)

# 3-3
cars = ['porsche', 'ferrari', 'bmw', 'lamborghini']
message = "I would like to race a"
print(message, cars[0].title())

motorcycles = []
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
motorcycles.append('kawasaki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles.insert(3, 'ferrari')
print(motorcycles)
del motorcycles[3]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = popped_motorcycle
print(f"The last motorcycle I owned was a {last_owned.title()}.")

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


# 3-8

world = ['singapore', 'china', 'japan', 'mexico', 'peru']
print(world)
print(sorted(world))
print(world)
world.reverse()
print(world)
world.reverse()
print(world)
world.sort()
print(world)
world.sort(reverse=True)
print(world)

print(len(world))

# Exercise 3 from Python Crash Course
# Guest List

guest_list = ['einstein', 'napoleon', 'cao cao']

message_1 = f"\nDear {guest_list[0].title()}, please attend our dinner this evening. Thank you."
message_2 = f"\nDear {guest_list[1].title()}, please attend our dinner this evening. Thank you."
message_3 = f"\nDear {guest_list[-1].title()}, please attend our dinner this evening. Thank you."

print(message_1, message_2, message_3)

# Changing Guest List

print(guest_list[0])

guest_list.insert(0, 'lincoln')

message_4 = f"\nDear {guest_list[0].title()}, please attend our dinner this evening instead."

print(message_4, message_2, message_3)

# More Guests
print("We have found a larger table for the dinner, so will be inviting additional guests.")
guest_list.insert(0, 'grant')
guest_list.insert(2, 'lee')
guest_list.append('churchill')

b = "\nDear"
e = ", please attend our dinner this evening."

print(guest_list)
print(b, guest_list[0].title()+e)
print(b, guest_list[1].title()+e)
print(b, guest_list[2].title()+e)
print(b, guest_list[3].title()+e)
print(b, guest_list[4].title()+e)
print(b, guest_list[5].title()+e)
print(f"{b} {guest_list[6].title()}{e}")

# Shrunk Guest List
announcement = "\nI can only invite two guests for dinner!"
print(announcement)

message_5 = "I am sorry, but you can no longer attend dinner"
u_1 = guest_list.pop()
print(f"\n{message_5} {u_1.title()}.")

u_2 = guest_list.pop()
print(f"\n{message_5} {u_2.title()}.")

u_3 = guest_list.pop()
print(f"\n{message_5} {u_3.title()}.")

u_4 = guest_list.pop()
print(f"\n{message_5} {u_4.title()}.")

u_5 = guest_list.pop()
print(f"\n{message_5} {u_5.title()}.")

invite = "\nYou are still invited tonight"
print(f"{invite} {guest_list[0].title()}.")
print(f"{invite} {guest_list[1].title()}.")

del guest_list[0]
del guest_list[0]
print(guest_list)
