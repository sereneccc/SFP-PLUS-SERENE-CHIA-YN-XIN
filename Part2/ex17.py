import random
name = input("What is your name?")
adjectives = ['Fearless', 'Sneaky', 'Brave', 'Silent', 'Fierce']
animals = ['Dragon', 'Otter', 'Tiger', 'Falcon', 'Wolf', 'Panther']
codename = random.choice(adjectives) + ' ' + random. choice(animals)
lucky_number = random.randint(1, 99)
print(f"{name}, your codename is: {codename}")
print(f"Your lucky number is: {lucky_number}")