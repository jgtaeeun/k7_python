# #part1-인수로 함수 들어가는 경우

# def ten_times(func):
#     for i in range(5):
#         func()

# def print_hello():
#     print("hello")

# ten_times(print_hello)       #함수를 인수로 전달

# #part2 -인수로 함수, 숫자 같이 들어가는 경우

# def add(x,y):
#     return x+y

# def apply_operation(operation, x, y) :
#     return operation(x, y)

# result=apply_operation(add,3,4)      #인수:함수,숫자,숫자
# print(result)

#part3 -map, filter
def power(item):
    return item**2

def under_three(item):
    return item<3

list_=[1,2,3,4,5]
map_list=map(power, list_)
print(list(map_list))

filter_list=filter(under_three, list_)
print(list(filter_list))

#part4 -람다식
m_list=map(lambda x:x*x, list_)
print(list(m_list))
