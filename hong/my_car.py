# from car2 import Car2      #car2.py파일로부터 Car2 클래스 import

# my_car=Car2('audi','a5',2024,'white')        #인스턴스 객체 생성
# print(my_car.get_descriptive_name())         #인스턴스객체.클래스메서드()
#  #2024식 audi제조사 a5모델명 white색

# from car2 import *      #car2.py파일로부터 모든 클래스(Car2,ElectricCar) import
# my_electriccar=ElectricCar('t','t5',2024,'brown')
# print(my_electriccar.get_descriptive_name())

import car2
my_car=car2.Car2('audi','a77',2024,'white') 
my_electriccar=car2.ElectricCar('t','t78',2024,'brown')
print(my_car.get_descriptive_name())
print(my_electriccar.get_descriptive_name())