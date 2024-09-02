import math
import random
def area(radius):
    print(f'半径を入力:{radius}')
    radius = int(radius)
    num = ("{:.0f}".format(radius * radius * 3.14))
    print(f'半径が{radius}の円の面積は{num}です。')
area('3')
def volume(height):
    print(f'高さを入力:{height}')
    height = int(height)
    num1 = ("{:.0f}".format(28 * height ))
    print(f'底面積が28で高さが{height}の円柱の面積は{num1}です。')
volume('10')