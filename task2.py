from random import randint


class SearchPoint():
    '''Класс искомой точки'''
    def __init__(self, w, h):
        '''
        инициализация случайных координат искомой точки
        '''
        self.__x = randint(0, w)
        self.__y = randint(0, h)

    def where_is_point(self, x, y):
        '''
        Описывает положение искомой точки относительно текущей.
        Возможные варианты: "R", "RU", "RD", "L", "LU", "LD", "U", "D" , ""
        '''
        pos_x = pos_y = ''
        if x > self.__x:
            pos_x = 'L'
        elif x < self.__x:
            pos_x = 'R'
        if y > self.__y:
            pos_y = 'D'
        elif y < self.__y:
            pos_y = 'U'
        return pos_x+pos_y

    
_, _, w, h = input().split() 
_, _, x, y = input().split()
w, h, x, y = int(w), int(h), int(x), int(y)
SP = SearchPoint(w, h)
x_min, x_max, y_min, y_max = 0, w, 0, h
    
vector = SP.where_is_point(x,y)

while vector:
    if 'R' in vector:
      x_min = x+1
    elif 'L' in vector:
      x_max = x-1
    else:
      x_max = x_min = x
    
    if 'U' in vector:
      y_min = y+1
    elif 'D' in vector:
      y_max = y-1
    else:
      y_max = y_min = y

    x = int((x_min + x_max) / 2)
    y = int((y_min + y_max) / 2)
    print(x, y)

    vector = SP.where_is_point(x,y)

print(f'Искомая точка: ({x}, {y})')

