class Car2 :
    """자동차 클래스"""
    def __init__(self, make, model,year,color) : #생성자(객체, 데이터 멤버)
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.odometer=0            #속성 odometer은 고정값으로 지정한다.
        self.tank=10

    def get_descriptive_name(self):        #클래스 메서드
        """자동차 객체 기술"""
        long_name=f"{self.year}식 {self.make}제조사 {self.model}모델명 {self.color}색"
        return long_name

    def update_odometer(self, mileage):         #속성 odometer 고정값을 수정한다.
        self.odometer=mileage

    def fill_gas_tank(self):
        """가스차의 연료통"""
        print(f"가스차의 연료통은 {self.tank}입니다.")

    def __str__(self): #__str__은 클래스의 인스턴스를 문자열로 변환하는 데 사용됩니다. 이 메소드를 구현하면 클래스의 인스턴스를 출력할 때 더욱 가독성 있는 출력을 제공할 수 있습니다.
        return f"[{self.make},{self.year}]"

class Battery():
    def __init__(self,battery_size=40):   #battery_size는 값이 없을 경우, 기본값 40을 갖는 옵션 매개변수이다.
        self.battery_size=battery_size


class ElectricCar(Car2):      #상속 :class 자식클래스명(부모클래스명):
    """슈퍼클래스의 subclass"""
    def __init__(self, make, model, year, color):
        ###superclass의 생성자 호출###
        super().__init__(make, model, year, color)
        self.battery=Battery()           #클래스 Battery()를  만든다. =>합성
    def fill_gas_tank(self):
        super().fill_gas_tank()
        print(f"전기차는 탱크 없음")
    



my_new_car=Car2('audi', 'a6',2024,'red')    #인스턴스 객체

print(my_new_car.get_descriptive_name())

my_new_car.color='green'          #속성 값 직접 수정하기
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(30)           #함수를 만들어서 함수를 통해 값 수정
print(my_new_car.odometer)


print(my_new_car.tank)

print(my_new_car) #출력하기 위해서 string필요>객체를 str로 변환 필요>__str__ 자동호출

my_new_electircar=ElectricCar('nissan','leaf',2024,'black')   #인스턴스 객체
my_new_electircar.fill_gas_tank()                     #부모메서드 오버라이드한 자식메서드

print(my_new_electircar.battery.battery_size)