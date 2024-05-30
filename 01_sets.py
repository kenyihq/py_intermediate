# Strings

set_countries = {"Perú", "Colombia", "Chile", "Mexico"}

print(set_countries)
print(type(set_countries))

# Numbers

set_numbers = {1, 2, 3, 4, 5}

print(set_numbers)
print(type(set_numbers))

# All

set_types = {'hola', 2, 3.4, True}
print(set_types)
print(type(set_types))


# From strings

set_from_string = set('hooola')
print(set_from_string)

# From tuples

set_from_tuple = set(('abc', 'def', 'hola', 'abc'))
print(set_from_tuple)

# Lists

my_numbers = 1, 2, 3, 4, 5, 4, 5

set_numbers = set(my_numbers)
print(set_numbers)

unique_numbers = list(set_numbers)
print(unique_numbers)