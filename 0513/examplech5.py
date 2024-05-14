# #5-1
# car='audi'
# if car=='subaru' : 
#     print("Is car == 'subaru' ? I predict True")
#     print(car=='subaru')
# elif car=='audi' :
#     print("\nIs car == 'audi' ? I predict False")
#     print(car=='audi')


# #5-3
# alien_color = 'yellow'
# if alien_color=='green' :
#     print('get 5 points')


# #5-4
# alien_color = 'yellow'
# if alien_color=='green' :
#     print('get 5 points')
# else :
#     print('get 10 points')

# #5-5
# alien_color = 'green'
# if alien_color=='green' :
#     print('get 5 points')
# elif alien_color=='yellow' :
#     print('get 10 points')
# else :
#      print('get 15 points')

# #5-6
# age = int(input())
# if age<2 : 
#     print('baby')
# elif age>=2 and age <4 :
#     print('toddler')
# elif age>=4 and age<13 :
#     print('kid')
# elif age>=13 and age<20 :
#     print('teenager')
# elif age>=20 and age<65 :
#     print('adult')
# elif age>=65  :
#     print('elder')
# else :
#     print('input error')


#5-7
# favorite_fruits =[]
# favorite_fruits.append('apple')
# favorite_fruits.append('strawberry')

# if 'apple' in favorite_fruits :
#     print('yes')
# if 'strawberry' in favorite_fruits :
#     print('yes')
# if 'banana' in favorite_fruits :
#     print('yes')

#5-8
# username=['a1','a2','a3','a4', 'admin']
# for i in username :
#     if i=='admin':
#         print('관리자님 안녕하세요.상태보고서를 보시겠습니까?')
#     else :
#         print(f'{i}님 안녕하세요.다시 로그인 해주셔서 감사합니다.')

#5-9
username=[]
if not username:
   print('사용자가 있어야 합니다.')


#5-10
current_list=['apple', 'banana','carrot', 'strawberry', 'orange']
new_list=['Apple', 'banana','yellow', 'green', 'red']   
# for i in new_list:
#    if i in current_list :
#       print('중복입니다. 새 사용자 이름을 입력하세요')
#    else :
#       print('사용가능한 사용자 이름입니다.')

# 중복입니다. 새 사용자 이름을 입력하세요
# 사용가능한 사용자 이름입니다.
# 사용가능한 사용자 이름입니다.
# 사용가능한 사용자 이름입니다.
# 사용가능한 사용자 이름입니다.

new_list1=[i.lower() for i in new_list]
print(new_list1)  
for i in current_list :
   if i.lower() in new_list1:
      print('중복입니다. 새 사용자 이름을 입력하세요')
   else :
      print('사용가능한 사용자 이름입니다.')
# 중복입니다. 새 사용자 이름을 입력하세요
# 중복입니다. 새 사용자 이름을 입력하세요
# 사용가능한 사용자 이름입니다.
# 사용가능한 사용자 이름입니다.
# 사용가능한 사용자 이름입니다.


#5-11
list_num=[1,2,3,4,5,6,7,8,9]

for i in list_num:
   if i==1:
      print(f'{i}st')
   elif i==2:
      print(f'{i}nd')
   elif i==3:
      print(f'{i}rd')
   else :
      print(f'{i}st')   