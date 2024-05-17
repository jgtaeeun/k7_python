# s=input()  #backjoon
# list_=[i for i in s]     # ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']
# tmp=list_[::-1]          #['n', 'o', 'o', 'j', 'k', 'e', 'a', 'b']



# i=0
# for _ in range(len(tmp)): # 리스트 길이 8=> 인덱스 0~7 /8번실행
#     if tmp[i]==list_[i] and i==len(tmp)-1 :
#         print("1")
#     elif tmp[i]==list_[i] :
#         i=i+1
#     else :
#         print('0')
#         break
#================================================================

s=input()  #baekjoon
count=[0 for _ in range(26)]    #알파벳 횟수 a~z까지[]
slist=[i for i in s]  #['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']

#알파벳을 아스키코드로 바꿈
#a,A=>count[0] 
#ord('A') >=65 and <=90 : count[ord('A')-65]=count[ord('A')-65]+1
#ord('a') >=97 and <=122 : count[ord('a')-65-32]=count[ord('a')-65]+1

for i in slist:
    if ord(i) >=65 and ord(i) <=90 :
        count[ord(i)-65]=count[ord(i)-65]+1
    elif ord(i) >=97 and ord(i)<=122: 
         count[ord(i)-97]=count[ord(i)-97]+1
    else :
        print('대소문자를 입력해주세요')


#최댓값일 때 알파벳을 출력
max=max(count)
fo=count.index(max)

i=0
for _ in count:
   if max!=count[i]:
       print('?')
       break
   else :
       i=i+1   
print(chr(fo+65))




