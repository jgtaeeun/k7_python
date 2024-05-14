from pizza import make_pizza     #from py파일명 import py파일의 함수명


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizza import make_pizza as mp     #from py파일명 import py파일의 함수명


mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')