import matplotlib.pyplot as plt

from random_walk_8 import RandomWalk_8


while True:
    # Make a random walk.
    rw = RandomWalk_8()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.set_xlabel("row",fontsize=14)
    ax.set_ylabel("col",fontsize=14)
    ax.set_title("3x3 matrix",fontsize=20)
    

    ax.scatter(rw.x_value,rw.y_value, color='black', s=1)   # 전체 점
    ax.scatter(rw.x_value[:1], rw.y_value[:1] ,color='red', s=1)   # 시작점 rw.x_value[], rw.y_value[]의 인덱스 0
    ax.scatter(rw.x_value[-1],rw.y_value[-1], color='yellow', s=1)   #끝점 rw.x_value[], rw.y_value[]의 인덱스 마지막
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break    