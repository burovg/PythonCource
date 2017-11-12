import math
grades = {1:[30,40,50],2:[70,60,80],"Anna" : [25,67,98]}

id = "Anna"

if id in grades:
    print(max(grades[id]))
