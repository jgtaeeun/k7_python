import random

# 두 세트 생성(이후 winnerset과 lottoset비교를 위한 틀 )
set1 = {1, 2, 3, 4, 5}             #set은  값 나열
set2 = {3, 2, 1, 5, 4}

# 두 세트가 동일한지 확인 (모든 요소가 같은지)
print("set1과 set2가 동일한지:", set1 == set2)     #set1의 요소와 set2의 요소가 일치할 때 True/그 외에는 False
print(set1.intersection(set2))             #교집합 {1,2,3,4,5}
print(len(set1.intersection(set2))==5 )    #True

#set1.intersection()
# 로또 복권 번호 생성 함수
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))       
    
    #  1부터 45까지의 숫자 중에서 무작위로 숫자 6개 선택(sample)하여 세트로 변환 (중복 없음)
    lotto_numbers = set(random.sample(numbers, 6))
    
    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)
    
    return lotto_numbers, bonus_number        #파이썬은 return타입이 없기에 return값이 타입이 다른 여러 개 가능하다.
def winner_check(lotto_numbers, lotto_bonus_number,winning_numbers, winning_bonus_number,idx):
    if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 1등 당첨!")
    elif lotto_numbers == winning_numbers:
        print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
    elif lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 + 보너스 번호 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 5:
        print(f"{idx}번째 로또 복권: 4등 당첨! (5개 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 4:
        print(f"{idx}번째 로또 복권: 5등 당첨! (4개 일치)")
    else:
        print(f"{idx}번째 로또 복권: 꽝")
    
# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers()      #파이썬에서는 다중할당 가능
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)

# 100장의 로또 번호 생성하여 당첨 여부 판별
lotto_list=[]
for idx in range(1, 101):
    lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
    #(lotto_numbers, lotto_bonus_number)
    #[(lotto_numbers, lotto_bonus_number),(lotto_numbers, lotto_bonus_number),''''']
    lotto_list.append((lotto_numbers, lotto_bonus_number))
    # 로또 번호와 보너스 번호가 당첨 번호와 일치하는지 확인(set1,set2 비교)
# print(lotto_list)

# 100장의 로또 번호 당첨 여부 판별   
# for idx in range(len(lotto_list)):
#     # print((lotto_list[idx])[0])
#     winner_check((lotto_list[idx])[0], (lotto_list[idx])[1],winning_numbers, winning_bonus_number)

#  ({5, 39, 9, 21, 24, 26}, 2) (a,b)꼴
idx=1
for a,b in lotto_list:   
     
     winner_check(a, b,winning_numbers, winning_bonus_number,idx)
     idx=idx+1

#   0 , ({5, 39, 9, 21, 24, 26}, 2) enumerate()
# for indexvalue ,number_set in enumerate(lotto_list):   
#     print(number_set)
#     for key, value in enumerate(number_set):
#         print(number_set[0],number_set[1])
#         winner_check(number_set[0], number_set[1], winning_numbers, winning_bonus_number, indexvalue+1 )
#         break