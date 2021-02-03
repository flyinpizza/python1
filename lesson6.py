# #1
# import time
# class TrafficLight:
#     __color = [["red", 7], ["yellow", 2], ["green", 11]]
#     def running(self):
#         for i in self.__color:
#             print(i[0])
#             time.sleep(int(i[1]))
# a = TrafficLight()
# a.running()

# #2
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#     def mass_calc(self, mass_per_msq, layer_cm):
#         return self._length * self._width * mass_per_msq * layer_cm
#
# road_90 = Road(2000, 20)
# print(f"{road_90.mass_calc(25, 1)} kg or {road_90.mass_calc(25, 1)/1000} tonns")

# #3
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage":wage, "bonus":bonus}
#
# class Position(Worker):
#     def get_full_name(self):
#         full_name = self.name + " " + self.surname
#         return full_name
#     def get_full_income(self):
#         full_income = sum(self._income.values())
#         return full_income
#
# worker_1 = Position("Bill", "Gates", "big boss", 300, 150)
# print(worker_1.get_full_name())
# print(worker_1.get_full_income())

# #4
# class Car:
#     def __init__(self, color, name, speed, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print("Go!")
#
#     def stop(self):
#         print("Stop!")
#
#     def turn(self, direction):
#         print(f'{"Left turn" if direction == 0 else "Right turn"}')
#
#     def show_speed(self):
#         print(self.speed)
#
# class TownCar(Car):
#     def __init__(self, color, name, speed = 60, is_police = False):
#         super().__init__(color, name, speed, is_police)
#     def set_speed(self, speed):
#         self.speed = speed
#         if self.speed > 60:
#                 print(f"{self.name} exceeded the permitted speed level")
#
# class SportCar(Car):
#     def __init__(self, color, name, speed = 200, is_police=False):
#         super().__init__(color, name, speed, is_police)
#
# class WorkCar(Car):
#     def __init__(self, color, name, speed = 40, is_police=False):
#         super().__init__(color, name, speed, is_police)
#     def set_speed(self, speed):
#         self.speed = speed
#         if self.speed > 40:
#             print(f"{self.name} exceeded the permitted speed level")
#
# class PoliceCar(Car):
#     def __init__(self, color, name, speed, is_police=True):
#         super().__init__(color, name, speed, is_police)
#
# coupe_car = Car("metallic", "Coupe", 80, False)
# lincoln = TownCar("rainy gray", "Lincoln", 58)
# print(lincoln.name)
# lincoln.set_speed(61)
# renault = WorkCar("beige", "Renault", 39)
# print((renault.is_police))
# renault.set_speed(70)

#5

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Запуск отрисовки маркером")

roller_pen = Pen("шариковая ручка")
roller_pen.draw()

whiteboard_marker = Handle("whiteboard marker")
whiteboard_marker.draw()

oil_pastel = Pencil("oil pastel")
oil_pastel.draw()