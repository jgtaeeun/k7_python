# data=[1,2,3]
# for d in data:
#     print(d,end=' ') #1 2 3  한줄로 출력
# print('-',data[1]) #1 2 3 - 2
# data[1]=5
# print('-',data[1])  #- 5      
# #----------------------------
# string = 'hello'
# for s in string:
#     print(s, end=' ')
# print('-' ,string[1])  #h e l l o - e
# #string[1]='H'       str은 대입연산자로 값 바꿀 수 없다.
# #----------------------------
# datatoople = (1,2,3)
# # for d in datatoople:
# #     print(d,end=' ') #1 2 3
# # #datatoople[1]=4    # 튜플도 대입연산자로 값 바꿀 수 없다.
# # #TypeError: 'tuple' object does not support item assignment

# # print(datatoople, type(datatoople)) #(1, 2, 3) <class 'tuple'>
# # #----------------------------
# # data2=[]
# # for i in datatoople :
# #     data2.append(i**2)
# # print(data2, type(data2)) #[1, 4, 9] <class 'list'>

# # data3=[i**2 for i in datatoople]         #이 방법으로 하면 코드 1줄로 리스트 생성할 수 있다.
# # print(data3, type(data3))  #[1, 4, 9] <class 'list'>

# # data4=[i**2 for i in datatoople if i**2 <5]    #조건문을 반복문에 추가
# # print(data4, type(data4))  #[1, 4] <class 'list'>
# # ----------------------------
# #자바 for문 (for i =0 ;i <10 ; i++)   값이 10개임을 알아야함
# # data = [1,2,3]  
# # for i in data:  값이 3개임을 몰라도, 심지어 데이터가 없더라도 에러가 나지 않음 /data 자리에 이후 배우는 numpy를 넣어도 실행된다.
# #     print(i)
# data = []  
# for i in data:  
#  print(i)
# # ----------------------------
# for  i in range(5):  
#  print(i, end=' ') #0 1 2 3 4   [0,5)

# for  i in range(1,5):  
#  print(i, end=' ') #1 2 3 4  [1,5)

# for _ in range(10):  
#  print('a', end=' ')  # a a a a a a a a a a 

# data = [1,2,3,4,5]
# for idx, d in enumerate(data):
#         print(idx, d)
#         #0 1
#         #1 2
#         #2 3
#         #3 4
#         #4 5

# ----------------------------
#파이썬 에러 안 나기 위해 for문 뒤 :세미클론 꼭 적기!/tab을 하여 코드를 어디부터 어디까지 실행할 것인지 잘 분류하기(루프블록 잘 묶기)
# data_2d=[[1,2,3],
#          [4,5,6]]
# for data in data_2d:
#    for d in data: 
#       print(d, end=' ')      #1 2 3 4 5 6

# #range(1,10)
# #1단부터 9단까지
# for i in range(1,10):
#   for j in range(1, 10):
#     #  print(i,'*',j ,'=', i*j)
#      print(f'{i}*{j}={i*j}')
#      print()
# #range(1,11)
# sum=0
# count=0
# max=1 
# min=10
# for i in range(1,11):
# #    sum=sum+i
# #    count=count+1
#     if i>max: 
#          max=i 
#     if i<min: 
#          min=i 
# # print(sum)
# # print(sum/count)
# print(max)
# print(min)

#for문없이 바로 구하는 방법
print(max(range(1,11)))
print(min(range(1,11)))
# ----------------------------
# data=range(1,1001) #1~1000
# # data=range(1,1001,2)     #1~1000까지의 홀수
# # data=range(2,1001,2) #1~1000까지의 짝수
# print(data, type(data))  #range(1, 1001)  <class 'range'>

# for d in data:
#    print(d, end=' ') 

# ----------------------------

#[1,11)
data=list(range(1,11))

#print(data, data[1:5], sep='\n')         #슬라이싱
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[2, 3, 4, 5]

#print(data, data[-1])  #리스트의 가장 마지막 끝값 출력

#print(data, data[:5],data[5:], sep='\n')      #반으로 나눌 때
#[1, 2, 3, 4, 5]
#[6, 7, 8, 9, 10]


#print(data, data[::-1], sorted(data, reverse=True), sep='\n')  #reverse할 때, 방법 2가지
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# ----------------------------
#swap

# def swap(a, b):
#     temp=a
#     a=b
#     b=temp
# a,b=1,2
# print(a, b) #1 2
# swap(a, b)
# print(a,b)  #1 2    

# def swap1(a, b):
#     temp=a
#     a=b
#     b=temp
#     return a, b
# a,b=1,2
# print(a, b) #1 2
# print(swap1(a, b)) # (2, 1)
# print(a,b)  #1 2   

# data=[1,2,3]
# data2=data
# data2[1]=5
# print(data, data2, sep='\n')
#[1, 5, 3]
#[1, 5, 3]


# data=(1,2,3)
# data=data[:]           #튜플, 문자열 리스트는 값 변경을 허용하지 않기에 재정의해야한다.  
# data[1]=5     #튜플은 값변경을 허용하지 않기에 data리스트를 튜플로 만들어 오류난 곳을 찾는다.
#data[1]=5
#TypeError: 'tuple' object does not support item assignment

# print(data, data, sep='\n')

# data=[1,2,3]
# data2=data.copy()                          #copy를 써서 인덱스 값에 값을 할당한다.
# data2[1]=5
# print(data, data2, sep='\n')
# #[1, 2, 3]
# #[1, 5, 3]

# data=[1,2,3]
# data2=data[:]    #슬라이싱을 써서 append로 값을 추가한다.
# data.append(4)
# data2.append(5)
# #[1, 2, 3, 4]
# #[1, 2, 3, 5]
# print(data, data2, sep='\n')

# ===========================================================================================================

#5장

# a=5  
# print(a==5)  #True
# print(a==1)  #False
# print(a!=5)    #False

#==,!= =>결과는 True, False
#>,<,>=  =>결과는 True, False
# string1='hello'
# string2='Hello'
# print(string1<string2)#False   아스키코드를 비교하는 것

# ---------------------------- 여러조건확인하기
# # score=int(input())       
# score=79    
# if (90<=score) and (score<=100) :        #if, elif, else 뒤에 꼭 세미콜론: 적기!
#     print('a')
# elif (80<=score) and (score<90) :        #자바: else if / 파이썬:elif
#     print('b')
# else :                                  
#     print('f')

# if 90<=score <100 :                    #에러는 나지 않으나 사용은 하지 말자
#     print('a')
# ----------------------------


#if문 안 조건(int, str, list의 ==동일한가)
# msg='hello'

# if msg=='hello' :
#     print('right')

# a=5
# if a==5:
#     print('right')

# data=[1,2,3]  
# if data==[1,2,3]:             #개수와 값들이 동일해야 한다. data=[1,2,3,4], data=[1,2,7]은 동일하지 않음 
#     print('right')


# a=3.14                      #실수형 float는 동등연산자를 쓰지 않는다.
# if a==3.14 :
#     print('right')


#data=[] 
#data=[1,2]
#if data:                       #list가 비어있지 않을 경우 , 실행된다.
#     print('right')


# ----------------------------
#값이 있는지 확인
# panda = 'fubao'          #문자열 안에 특정문자가 있는지 확인하는 if문
# if 'f' in panda:
#     print('here!')

# num=[1,2,3]
# if 4 in num :        #리스트 안에 특정숫자가 있는지 확인하는 if문
#     print('here')

#-------------------
#or연산
# a=15
# if a<5 or a>10 :      #01 10 11일 때
#     print('01일 때')
# a=7
# if not (a<5 or a>10) :    #00일 때
#     print('00일 때')
# #-------------------

print(1+2) #3
print(1<2) #True
print(sum([True,True,False]))  #2


if 1+2 :        
    print('aaa')      # aaa나옴, 하지만 if조건식에 true, false가 나오는 조건식을 쓰자

if 1-2 :
    print('AAA')      # AAA나옴, 하지만 if조건식에 true, false가 나오는 조건식을 쓰자

if 1<2 :             #if조건식에 true, false가 나오는 조건식을 쓰자
    print('1<2이다.')

# #-------------------
#특별요소 확인하기
data = [1,2,3]
for d in data:
    if d<2 :
        print(d)   
    else :
        print('wrong')
#1
#wrong
#wrong

#-------------------
