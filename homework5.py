my_list = ["apple", "banana", "orange", "kiwi", "apricot", "cherry", "limon", "pear"]
print("Список фруктов      :", my_list)
print("Первый элемент      :", my_list[0])
print("Последний элемент   :", my_list[-1])
print("Со третьего по пятый :", my_list[2:5])     # У шестого элемента пятый индекс
my_list[2] = "peach"                              # Замена третьего элемента  
print("Список фруктов      :", my_list)           # Список изменённый
print("\n")
my_dict = {"apple" :"яблоко", "banana" : "банан", "kiwi" : "киви", "apricot" : "абрикос"}
my_dict["cherry"] = "вишня"
print(my_dict)
print("Apricot с английского на русский: ", my_dict["apricot"])
my_dict.update({"limon" : "лимон", "pear" : "груша"})
print(my_dict)
