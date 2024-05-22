from random import choice
import math

class RandomWalk_8:
    def __init__(self):
        #list[list,list,list]      1,1에서 시작
        self.x_value=[1]
        self.y_value=[1]
        self.mat=[(1,1)]
    def fill_walk(self):
        while True:

            x_direction = choice([1, 0,-1])
            x_distance=x_direction+self.x_value[0]
            y_direction = choice([1,0, -1])
            y_distance=y_direction+self.y_value[0]
            
            if (abs(x_distance-1) + abs(y_distance-1) )<=2 :
                 if not (x_distance, y_distance) in self.mat:
                    self.mat.append((x_distance, y_distance))
                    self.x_value.append(x_distance)
                    self.y_value.append(y_distance)

            if len(self.x_value)==9 and len(self.y_value)==9 :
                print(self.x_value)
                print(self.y_value)
                break
            
            

            