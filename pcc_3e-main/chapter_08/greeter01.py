def greet_user():
    """Display a simple greeting"""         #함수가 수행하는 작업을 설명하는 독스트링이라는 주석이다.  보통 세개의 따옴표로 감싸며, 여러행에 걸쳐 쓸 수 있다.
    print("hello")

greet_user() 
#hello

help(greet_user)        #greet_user함수가 뭔지 설명부탁하는 것
#Help on function greet_user in module __main__:

# greet_user()
#     Display a simple greeting


print(greet_user.__doc__)            #독스트링이 출력된다.
#Display a simple greeting