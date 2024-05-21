
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots() #fig는 그래프 나오는 창 /ax는 그래프 하나
ax.plot(squares)

plt.show()