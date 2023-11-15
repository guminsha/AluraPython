# Will change my mutable list

# def process_list_view(my_list):
# 	print(len(my_list))
# 	my_list.append(13)

# Only creates the list once so it keeps append if called more than one time

# def process_list_view(my_list = []):
# 	print(len(my_list))
# 	print(my_list)
# 	my_list.append(13)

# Solves the multiple recurrent append

def process_list_view(my_list = None):
	if my_list == None:
		my_list = list()
	print(len(my_list))
	print(my_list)
	my_list.append(13)


ages = [16, 21, 29, 56, 43]
process_list_view()
process_list_view()
process_list_view()
print(ages)