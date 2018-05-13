import random

# m = ['a','b','c','d','e']
#
# print(random.randint(1,1000))
#
# print(random.choice(m))
#
#
# n = {}
#
#
# n[random.choice(m)] = random.randint(100,10000)
#
# print(n)






'''
Генератор случайных машин
'''


# cars = []
#
# models = ['BMW', 'Toyota', 'Mercedes', 'Audi', 'VW', 'GMC', 'Opel', 'Nissan']
# colors = ['White', 'Black', 'Blue', 'Grey', 'Red', 'Green', 'Yellow']
#
#
# for i in range (random.randint(10,20)):
#
#
#     cars.append( {
#         "Model": random.choice(models),
#         "Year": random.randint(1992,2018),
#         "Price":random.randint(500000,5000000),
#         "Color":random.choice(colors)
# })
#
# for car in cars:
#     for key, value in car.items():
#         print(key,value)
#     print("-----------------")



cars = []
#
models = ['BMW', 'Toyota', 'Mercedes', 'Audi', 'VW', 'GMC', 'Opel', 'Nissan']
colors = ['White', 'Black', 'Blue', 'Grey', 'Red', 'Green', 'Yellow']



def generate_car(models, colors, years, prices):
    return {
        "Model": random.choice(models),
        "Year": random.randint(years[0], years[1]),
        "Price":random.randint(prices[0],prices[1]),
        "Color":random.choice(colors)
    }


def generate_random_cars(models, colors, years, prices, count):
    res = []

    for i in range(random.randint(1,count)):
        res.append(generate_car(models, colors, years, prices))
    return res

def print_car(car):
    for key, value in car.items():
        print(key, value)

def print_cars(cars):
    for i in cars:
        print_car(i)
        print("-----------")

cars = generate_random_cars(models, colors, (1992, 2018), (50000,600000000), 30)

print_cars(cars)

