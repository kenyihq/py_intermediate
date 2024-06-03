# generate dictionary

dict = {}
for i in range(5):
    dict[i] = i*2

print(dict)

# dict comprehension

dict_02 = { i: i*2 for i in range(5) }

print(dict_02)

# generate dictionary 
import random


countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)


print(population)

# Dict comprehension

population_v2 = { country: random.randint(1, 100) for country in countries}

print(population_v2)

# join lists

names = ['Kenyi', 'Axel', 'Ariana']
ages = [30, 15, 10]

print(list(zip(names, ages)))

print_dict = {name: age for (name, age) in zip(names, ages)}

print(print_dict)