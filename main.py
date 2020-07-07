def print_valid_cities(all_cities, used_cities):
    print(all_cities.difference(used_cities))
all_cities = set([
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
])

used_cities = set(['Калуга', 'Абакан' , 'Новосибирск'])


print_valid_cities(all_cities, used_cities)