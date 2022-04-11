###################################################   1
my_list = ["qwe", "rty", "uio", "asd"]
new_list = []
for index, symbol in enumerate(my_list):
    if index % 2:
        new_list.append(symbol[::-1])
    else:
        new_list.append(symbol)
print(new_list)
#####################################################  2
my_list = ["qwe", "aty", "uio", "asd"]
new_list = []
for symbol in my_list:
    if symbol[0] == "a":
        new_list.append(symbol)
print(new_list)
####################################################   3
my_list = ["qwe", "ray", "uio", "asd"]
new_list = []
for symbol in my_list:
    if symbol.count("a"):
        new_list.append(symbol)
print(new_list)

###################################################    4
persons = [ {"name": "Jhon", "age": 20},
            {"name": "Jacki", "age": 15},
            {"name": "Billi", "age": 10},
            {"name": "Mel", "age": 45},
          ]
###############################################    a
list_age = []
list_name = []
for my_dict in persons:
    list_age.append(my_dict["age"])
min_age = min(list_age)
for my_dict in persons:
    if my_dict["age"] <= min_age:
        list_name.append(my_dict["name"])
print(list_name)
#############################################      b
list_len = []
list_long_name = []
for my_dict in persons:
    list_len.append(len(my_dict["name"]))
max_long = max(list_len)
for my_dict in persons:
    if len(my_dict["name"]) >= max_long:
        list_long_name.append(my_dict["name"])
print(list_long_name)
#############################################     c
list_age = []
for my_dict in persons:
    list_age.append(my_dict["age"])
print("среднее количество лет = ", sum(list_age)/len(list_age))

###################################################################      5

#############################################################    a
my_dict_1 = {1:1, 2:2,}
my_dict_2 = {11:11, 2:22}
my_list = []
for key_1 in my_dict_1.keys():
    for key_2 in my_dict_2.keys():
        if key_1 == key_2:
            my_list.append(key_1)
print(my_list)
###########################################################      b
my_dict_1 = {1:1, 2:2}
my_dict_2 = {11:11, 2:22}
my_list = []
for key in my_dict_1.keys():
        if key not in my_dict_2.keys():
            my_list.append(key)
print(my_list)
###########################################################       в
my_dict_1 = {1:1, 2:2}
my_dict_2 = {11:11, 2:22}
my_new_dict = dict()
for key, values in my_dict_1.items():
    if key not in my_dict_2.keys():
        my_new_dict.update({key:values})
print(my_new_dict)
###########################################################        г
my_dict_1 = {1:1, 2:2}
my_dict_2 = {11:11, 2:22}
my_new_dict = dict(list(my_dict_1.items()) + list(my_dict_2.items()))
for key in my_new_dict:
    if key in my_dict_1 and key in my_dict_2:
        my_new_dict[key] = [my_dict_1.get(key), my_dict_2.get(key)]
print(my_new_dict)
