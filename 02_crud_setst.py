set_countries = {'col', 'pen', 'mex'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('bol' in set_countries)

# add
set_countries.add('bol')
print(set_countries)

# update

set_countries.update({'arg', 'bra'})
print(set_countries)

# remove

set_countries.remove('bol')
print(set_countries)

# remove if doesn't exist

set_countries.discard('cl')
print(set_countries)

# remove all

set_countries.clear()
print(set_countries)
print(len(set_countries))