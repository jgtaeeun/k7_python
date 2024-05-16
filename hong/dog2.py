#9장 클래스

class Dog2:
    """클래스 Dog 정의"""

    def __init__(self, name, age): #생성된 객체 self// 데이터멤버(자바라고 보면 필드부분) name,age
        """클래스 Dog의  생성자"""    #__    __ 언더바 2개는 자동호출을 의미한다.
        self.name=name          #인수로 받은 값 name을 데이터멤버에 넣는다.
        self.age=age            #인수로 받은 값 age를 데이터멤버에 넣는다.
        # self.city='busan'    인수로 받지 않고 고정적인 값 'busan'으로 데이터멤버city를 정한다.

    def sit(self):           #클래스 Dog2의 메서드를 함수로 정의함
        """개가 앉기 동작"""
        print(f"{self.name}가 앉아 있다.")

myDog=Dog2("hong",10)     #클래스에서 인스턴스 만들기(메모리에  데이터멤버 할당/데이터멤버를 묶는 객체 할당(self))
#self는 인스턴스 자체를 나타내며 인스턴스와 연관된 메서드는 모두 self를 자동으로 전달한다. 

myDog.sit()

## self의 의미

## self는 인스턴스 자기 자신을 의미합니다.

# 인스턴스가 생성될 때 self.name=name ,self.age=age처럼 자기 자신에 속성을 추가했다

# 여기서 __init__의 매개변수 self에 들어가는 값은 Dog2()이라 할 수 있다. 

# 그리고 self가 완성된 뒤 myDog에 할당되고 

# 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어온다. 그래서 sit 메서드에서  print(f"{self.name}가 앉아 있다.")을 출력할 수 있는 것이다.