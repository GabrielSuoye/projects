# Sets use {} and can be changed but their order is not saved on memory, also sets can't contain dulicates.

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set))
my_set.discard(5)
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([5, 7, 8])
print(my_set)
my_set.clear()
print(my_set)

# Tuples use () and are immutable (cannot be changed).

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[2])
