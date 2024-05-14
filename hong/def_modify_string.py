# def modify_string(s):   
#     s = s+"world"
#     print(f"함수내출력{s}")

# st="hello"
# modify_string(st) #str을 전달하므로 str은 immutable객체이므로 함수종료 후에도 값이 변하지 않고 유지된다.
# print(st)

# def modify_num(s):   
#     s+=1
#     print(f"함수내출력{s}")


# num=10
# modify_num(num)
# print(num)

def modify_boolean(s):   
    if s:
        s=False
    else :
        s=True
    print(f"함수내출력{s}")


b=True
print(b, type(b))
modify_boolean(b)
print(b)