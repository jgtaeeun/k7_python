import random

# 빈 리스트 생성
random_numbers = []

# 난수를 20개 생성하여 리스트에 추가
for _ in range(20):
    random_numbers.append(random.randint(1, 100))  # 1부터 100 사이의 난수 생성해서 추가

# 저장된 리스트 출력
print(f"난수 생성 = {random_numbers}")
# s 다음에 숫자를 가진 변수들을 생성하여 리스트에 저장하는 예제

# 빈 리스트 생성
string_list = []

# s 다음에 숫자를 가진 변수들 생성하여 리스트에 추가: s1, s2, s3 등을 생성 

for i in range(1, 21):
   string_list.append("s" + str(i))

# 저장된 리스트 출력
print(f"sno 리스트 = {string_list}")

students = string_list              #['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20']
scores = random_numbers             #[29, 51, 68, 25, 63, 55, 87, 2, 44, 55, 60, 31, 50, 8, 47, 89, 98, 72, 23, 35]

# students, scores로 구성된 딕셔너리를 만든다
score_dic = { }

for i in range(20) :
        score_dic[students[i]]=scores[i]
#{'s1': 3, 's2': 51, 's3': 40, 's4': 21, 's5': 7, 's6': 93, 's7': 86, 's8': 32, 's9': 10, 's10': 24, 's11': 89, 's12': 29, 's13': 67, 's14': 75, 's15': 44, 's16': 74, 's17': 58, 's18': 86, 's19': 36, 's20': 18}
print(f"학번과 점수 딕셔너리={score_dic}")


# 점수를 기준으로 내림차순으로 정렬한 튜플 리스트 생성 
sorted_scores = sorted(score_dic.items(), key=lambda x: x[1], reverse=True)       #람다식 사용

print(f"내림차순으로 정렬된 학번과 점수 튜플 리스트 = {sorted_scores}")

# 정렬된 튜플 리스트를 다른 딕셔너리에 저장
sorted_score_dic = {}
for i in range(20) :
        sorted_score_dic[(sorted_scores[i])[0]]=(sorted_scores[i])[1]

# 결과 출력
print(f"점수로 정렬된 딕셔너리= {sorted_score_dic}")

# 정렬된 튜플 리스트에서 상위 5개 추출하여 리스트로 저장
# 상위 5개 추출하여 딕셔너리로 저장

top_5 = {}    #sorted_scores.slice(:5)
for i in range(5) :
      top_5[sorted_scores[i][0]]=sorted_scores[i][1]

# 결과 출력
print(f"상위 5개= {top_5}")

# 딕셔너리의 키-값 쌍을 튜플로 묶어 리스트에 추가
score_list = []
score_list =sorted(top_5.items(), key=lambda x: x[1], reverse=True)
       
# 결과 출력
print(f"리스트로 변환된 딕셔너리: {score_list}")
# 딕셔너리의 각 요소를 enumerate를 사용하여 변환
transformed_score_dic = {}

for idx, keyvalue in enumerate(score_list):
    # print(idx, keyvalue )
    transformed_score_dic [idx]=keyvalue
# # 결과 출력
print(f"변환된 딕셔너리: {transformed_score_dic}")