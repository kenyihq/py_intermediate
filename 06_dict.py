import random

countries = ['col', 'mex', 'bol', 'pe']

population = { country: random.randint(1, 100) for country in countries}


print(population)