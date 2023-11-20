users = {1, 5, 76, 34, 52, 13, 17}
users.add(13)
print(users)

users = frozenset(users)
print(f"{type(users)} | {users}")

text_sample = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
text_sample = text_sample.lower()
set_text_sample = set(text_sample.split())

appers = {}

for word in text_sample.split():
	until_now = appers.get(word, 0)
	appers[word] = until_now + 1

print(appers)



#---------------------------------------------------------------------------------
# dict1 = dict(John = 1, Paul = 2, Logan = 7)
# print(dict1)
# dict2 = {"John": 1, "Paul": 2, "Logan": 7}
# del dict2["John"]
# print(dict2)

# print("Paul" in dict2)

# for key, value in dict2.items(): # dict2.values() / dict2.keys()
# 	print(key,"=",value)

# # using list comprehension
# list_names = [f"Key: {key} Value:{value}"for key, value in dict2.items()]
# print(list_names)
#-----------------------------------------------------------------------------------

