from random import randint
from random import choice 

print(randint(1,6))

players = ['a','b','c','d','e','f']
print(choice(players))

#class 변수
class Student:
    count=0                #count가 클래스 변수
    def __init__(self):    #클래스 생성자
        Student.count+=1   #count클래스 변수값 변경
    @classmethod           #클래스 메소드 사용
    def printing(self):
        print(f"클래스메소드 출력={Student.count}")

print(f"{Student.count}")

s1=Student()      #인스턴스 객체
print(f"{Student.count}") 
Student.printing()        #클래스 메소드 호출     클래스메소드 출력=1

s2=Student()      #인스턴스 객체
print(f"{Student.count}")
Student.printing()        #클래스 메소드 호출     클래스메소드 출력=2

def initialize():
    return 1,2,3

_,a,b = initialize()   #다중 할당
print(a,b)   #2 3

a=[1,2,3]
b=[4,5,6]

mergeList=[*a,*b] #*기호는 iterable객체를 나타내고 unpacking/*는 리스트이다. 즉 리스트a,리스트b를 풀어서 전체리스트를 나열한다.
print(mergeList)  #[1, 2, 3, 4, 5, 6]

#class instance에 대한 인덱싱과 슬라이싱 처리
class MyList:
    def __init__(self,data):
        self.data=data

    def __getitem__(self, index):
        return self.data[index]
    
mlist=MyList([1,2,3,4])
print(mlist[1:3])   #슬라이싱을 위한  __getitem__ 자동호출

s=['s1','s2','s3']
num=[5,3,7]
score=zip(s,num)     #   zip (s1,5)(s2,3)(s3,7)

for a, b in score:
    print(f"[{a},{b}]")

