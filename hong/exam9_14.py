from random import randint

nlist=[randint(1,45) for _ in range(10)]


print(nlist)


total_list=[*nlist , *slist]
