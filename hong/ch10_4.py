#10-4 연습문제

print("사용자이름: ")
name=input()
with open ('guest.txt', 'w') as file:
    file.write(name)