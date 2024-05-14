


# #4-1
# pizza=['페퍼로니', '포테이토']   #str일 경우, ''로 감싸기!!!!!
# for i in pizza:
#     print(f'나는 {i} 피자가 좋습니다.')
# print('나는 피자를 정말 사랑합니다.')

# #4-2
# panda=['아이바오', '러바오', '푸바오', '루이바오', '후이바오']
# for i in panda:
#     print(f'{i}는 강바오를 좋아합니다.')
# print('이 동물들은 모두 귀엽습니다.')
    

# #4-3
# sum=0     #sum초기화 필수!
# for i in range(1,21):
#     sum=sum+i
# print(sum)  #210

#4-4  #4-5
# numlist=[] 
# for i in range(1,101):
#     numlist.append(i)
# print(numlist)
# print(min(numlist))
# print(max(numlist))
# print(sum(numlist))

#범위값을 입력으로 주면 sum, max,min함수로 값을 바로 구할 수 있다.
print(sum(range(1,101)))  #5050
print(max(range(1,101)))  #100
print(min(range(1,101)))  #1

# #4-6
# list_odd=[]
# for k in range(1,21,2):
#     list_odd.append(k)
# print(list_odd) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# for k in list_odd:
#     print(k)

# #4-7
# list_3=[]
# for j in range(3, 31, 3):
#     list_3.append(j)
# print(list_3)
# for j in list_3:
#     print(j)

# #4-8 *4-8과 같이 코드 짜는 거 중요-리스트 만들고 반복문 돌면서 리스트 값 추가시키는 거 -코드 틀 외우기*
# list_4_8 =[]
# for i in range(1,11):
#   list_4_8.append(i**3)
# print(list_4_8)


# #4-9   리스트 내포
# list_calc=[i**3 for i in range(1,11)] 
# print(list_calc)  #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# for i in list_calc:
#     print(i,  end=' ') # 1 8 27 64 125 216 343 512 729 1000


#4-10
list_1to10=[]
for k in range(1,10):
    list_1to10.append(k)
print(list_1to10)
print("리스트의 첫 세항목은 :")
print(list_1to10[:3])
print(list_1to10[3:6])
print(list_1to10[6::])

#4-11  
#4-12 
pizza=['페퍼로니','포테이토']
pizza_copy=['페퍼로니','포테이토']
pizza.append('불고기')
pizza_copy.append('하와이안')
print(pizza)
print(pizza_copy)

for i in pizza :
    print(f'내가 좋아하는 피자는 {i}')
for i in pizza_copy:
    print(f'내 친구가 좋아하는 피자는 {i}')






