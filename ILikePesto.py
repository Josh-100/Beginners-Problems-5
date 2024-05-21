iLikePesto = []
otherFoods = []

for i in range(8):
    food = input(f"Person {i+1}, what is your favorite food? ").strip().lower()
    if food == 'pesto':
        iLikePesto.append(food)
    else:
        otherFoods.append(food)

pesto_count = len(iLikePesto)
print(f"Pesto is mentioned: {pesto_count}")

for _ in range(pesto_count):
    print("I like pesto")

print("List of other foods:", otherFoods)