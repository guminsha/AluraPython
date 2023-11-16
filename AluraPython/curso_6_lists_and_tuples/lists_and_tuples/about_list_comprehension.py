itens_shop = ["Apples", "Bananas", "Milk", "Bread", "Eggs", "Cheese", "Tomatoes", "Potatoes", "Chicken", "Rice"]

my_list = [item for item in itens_shop if item[0].upper() in ["A", "C", "M"]]
my_list.sort()

print(my_list)