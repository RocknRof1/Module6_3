class Vehicle:
    vehicle_type = 'none'

class Car:
    price = 1000000

    def horse_power(self, horse_power):
        self.horse_power = horse_power
        print(f'Мощность двигателя: {self.horse_power} л.с.')
        return self.horse_power

class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 2000000
        self.vehicle_type = 'Teana'
        self.horse_powers = 175


nissan = Nissan()

print(f'Тип машины: {nissan.vehicle_type}')
print(f'Стоимость: {nissan.price}')
print(f'Лошадиные силы: {nissan.horse_powers}')
