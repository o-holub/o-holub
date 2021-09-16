# 1st Lesson
print(1+1)
print(2+3)
print(1==1)
print(6/3)
print(6//3)
print('Bear')
print('Hello')
# Программа для зоопарка
# Сохранять животных разных видов
# Нужно знать, чем кормить каждого животного
print('kind')
print('kind "Bear"')
print("Медведь")
print("Boris")
print("Медведь 'Boris'")
print('Медведь "Boris"')
print(1==1)
print(1//1)
print(1/1)
print("kind")
print("kind = Медведь")
'Медведь'
kind = 'Медведь'
name = 'Миша'
age = 11
weight = 20.7
is_male = True

# список, словарь, множество, кортеж
kinds = ['Bear', 'Fox', 'Rabbit', 'Python', 'Crocodile']

animals = [{
    'name': 'Миша',
    'age': 11,
    'is_female': True,
    'kind': 'Bear',
    'weight': 116
},
{
    'name': 'Сергей',
    'age': 12,
    'is_male': True,
    'kind': 'Crocodile',
    'weight': 300
},
{
    'name': 'Слвва',
    'age': 27,
    'is_male': True,
    'kind': 'Python',
    'weight': 78
}
]

roles = ('Администратор', 'Директор', 'Наемники','Муравьи')

if len(animals) > 3:
    print('Московский')
else:
    if (len(roles) < 5) or ('Python' in kinds):
        print('Горловский')
    else:
        print('Скоро откроется')

if (animals[0]['weight']+animals[1]['weight']+animals[2]['weight']) > 500:
    print('Московский')
else:
    if (animals[2]['weight']) > 85:
        print('Питон Слава потолстел')
    else:
        print('Вес питона в норме')
print(type(animals))
print(type(roles))
print(type(kinds))
print(6//3)
2
print(type(2))
2.0
print(type(2.0))
print(type(3.0))
print(type("Медведь"))
print(type(is_male))
