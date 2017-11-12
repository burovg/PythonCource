import math
num = input("Enter array length: ")
arr = []
for i in range(num):
    arr.append(input("Enter value for index " + str(i)))

x = input("Enter x: ")

for i in range(3,num):
    if arr[i] < 5:
        arr[i] = arr[i] + x
    else:
        if arr[i] >= 6 and arr[i] <= 10:
            arr[i] = arr[i] * x
        else:
            if arr[i] > 10 :
                #c = arr[i]
                #for j in range(x):
                #    arr[i] = arr[i] * c
                arr[i] =arr[i] ** x
print(arr)





