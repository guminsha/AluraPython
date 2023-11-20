users_data_science = [15, 23, 43, 56]
users_machine_learning = [13, 23, 56, 42]

users_join = users_data_science.copy()
users_join.extend(users_machine_learning)
users_join = set(users_join)

print(users_join)
# if order doesnt matters, sets is better sometimes
# there is no index

for users in users_join: # But its a iterable
	print(users)

# extend in set
users_or = set(users_data_science) | set(users_machine_learning)
print(users_or)

# ... in set
users_and = set(users_data_science) & set(users_machine_learning)
print(users_and)

# ... in set
users_not_in_ml = set(users_data_science) - set(users_machine_learning)
print(users_not_in_ml)

print(15 in users_not_in_ml)

# excluiding in set
users_in_one_not_in_other = set(users_data_science) ^ set(users_machine_learning)
print(users_in_one_not_in_other)


