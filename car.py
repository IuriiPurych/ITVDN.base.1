class Car:
    name = str
    model = str
    color = str
    price = int

    def __init__(self, name, model, color, price):
        self.name = name
        self.model = model
        self.color = color
        self.price = price

    def __repr__(self):
        return '%s, %s, %s, %d' % (self.name, self.model, self.color, self.price)


class CarDealerShip:
    cars = []

    def add(self, car):
        self.cars.append(car)

    def list_of_cars(self):
        print('Cars list:')
        if len(self.cars) == 0:
            print('There are no cars.')
            return
        else:
            for car in self.cars:
                print('%s' % car.__repr__())
        print('-----------------------')

    def buy(self, car):
        if car in self.cars:
            print('The % sold.' % car.__repr__())
            self.cars.remove(car)
        else:
            print('There is no such %s in the showroom' % car.__repr__())

    def __repr__(self):
        return self.cars


car1 = Car('Ford', 'Focus', 'black', 24500)
car2 = Car('Citroen', 'Cactus', 'red', 17500)

dealership = CarDealerShip()
dealership.list_of_cars()
dealership.add(car1)
dealership.add(car2)
dealership.list_of_cars()

dealership.buy(car1)
dealership.buy(car1)
dealership.list_of_cars()
