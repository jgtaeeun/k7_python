from random import randint

class Dice :
    def __init__(self,sides=6) :
        self.sides=sides

    def roll_dice(self):
        for _ in range(10):
         print(randint(1,self.sides),end=' ')

sixdice=Dice()
sixdice.roll_dice()
# for _ in range(10):
#     sixdice.roll_dice()
print()
tendice=Dice(10)
tendice.roll_dice()

print()
twentydice=Dice(20)
twentydice.roll_dice()

