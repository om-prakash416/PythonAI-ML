#key:value pairs

my_dict = {
    "name": "monu",
     "name2": "",
    "age": 25,
    "city": "gaya"
}

print(my_dict)

print(type(my_dict))
print(my_dict["name"])

dict_keys = my_dict.keys()
print(dict_keys)

dict_values = my_dict.values()
print(dict_values)

dict_items = my_dict.items()
print(dict_items)
dict_length = len(my_dict)
print("Length of dictionary is ", dict_length)

print(my_dict.get("name"))
print(my_dict.get("name", "not found"))

print(my_dict.get("name1"))
print(my_dict.get("name1", "not found"))


dic_val_list = list(my_dict.values())
print(dic_val_list)

#methods on dictionary
