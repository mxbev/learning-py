magicians = ['alice', 'david', 'henry']
for magician in magicians:
    print(f"{magician.title()}, that was a great performance!")
    print(f"I can't wait to see your next show, {magician.title()}.\n")
print("Thank you",
f"{magicians[0].title()}, {magicians[1].title()} and {magicians[-1].title()}."
,"That was a great show!")

# 4-1
pizzas = ['margharita', 'la reine', 'pepperoni']
for pizza in pizzas:
    print(f"I would like a pizza {pizza} please.")
print("\nI love pizza more than anything.")

# 4-2
animals = ['cats', 'dogs', 'hamsters', 'grizzly bears']
for animal in animals:
    print(f"{animal.title()} make great pets")
print("Common pets include the above species.")

# 4-3
for value in range(1,21):
    print(value)

# 4-4
numbers = list(range(1, 1_000_001))
for number in numbers:
    print(number)

# 4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6
odds = list(range(1, 21, 2))
for odd in odds:
    print(odd)

# 4-7
threes = [value*3 for value in range(1, 11)]
for three in threes:
    print(three)

# 4-8
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)

# 4-9
# see above

# 4-10
print(f"The first 3 items are: {numbers[:3]}")
print(f"The last 3 items are: {numbers[-3:]}")

# 4-11
friend_pizzas = pizzas[:]
pizzas.append('cucina')
friend_pizzas.append('proscuitto')
print(pizzas)
print(friend_pizzas)

#4-12
foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
for food in foods:
    print(food)

