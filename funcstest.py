

import Canvas
import Tkinter

top = Tkinter.tk



def Add (num1,num2):
    return num1 + num2

def mult(num1,num2):
    return num1*num2

def half(num):
    if num <> 1:
        print num
        half(num/2)


def a(num):
    return num*2
def b(obj,num):
    return obj(num)

def count(lst):
    return len(lst)
def callcount(obj,lst):
    return obj(lst)

lst = [1,2,3,4,5]
print callcount(count,lst)

z = b(a,45)
print z

a = Add(12,3)
print a

a = mult(23,45)
print a

half(64)
