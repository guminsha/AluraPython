ages = [15, 86, 23, 29, 85, 43, 56, 23]

# for i in range(len(ages)):
# 	print(i, ages[i])

print(range(len(ages))) # Lazy
print(list(range(len(ages)))) # Forced the creation of values

print(enumerate(ages))
print(list(enumerate(ages)))

for index, age in enumerate(ages):
	print(f"Index: {index} Age: {age}")

users = [("Brian", 26, 1997), ("Leonardo", 27, 1997), ("Evandro", 27, 1996)]
for name, _, _ in users:
	print(name)

# --------------------------------------------------- Sorting

print(sorted(ages)) # Returns a list sorted
print(list(reversed(sorted(ages))))
print(sorted(ages, reverse=True))

ages.sort() # changes at the variable
print(ages)

# ---------------------------------------------------- Sorting but not in a natural way

names = ["Brian", "Evandro", "Leonardo", "aron"] # ascii
sorted(names)
print(names)