#2
my_dict = {"Alena" : 89898347823, "Kristina" : 98326355233 }
print(my_dict["Kristina"])
my_dict["Igor"] = 893467343
print(my_dict["Igor"])
my_dict.update({"Anton" : 898432342, "Sergey" : 893987323})
print(my_dict)
print(my_dict["Alena"])
print(my_dict)
del my_dict["Alena"]

#3
my_set = {1,1,1,1,3,3,3,6,6,5,5,5}
print(my_set)
print(my_set.add(8))
print(my_set.add(9))
print(my_set)
print(my_set.discard(5))
print(my_set)