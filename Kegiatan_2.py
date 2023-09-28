random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_dict = {}
float_tuple = ()
string_list = []

for item in random_list:
    if isinstance(item, int):
        int_dict[item] = tuple(map(int, str(item)))
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        string_list.append(item)

print("Nilai Integer dalam Dictionary:", int_dict)
print("Nilai Float dalam Tuple:", float_tuple)
print("Nilai String dalam List:", string_list)
