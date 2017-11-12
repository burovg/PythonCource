arr = []*0
cont = True

while True:
    num = input("Enter: ")
    if num < 10:
        if not num in arr:
            arr.insert(0,num)
            print arr
    else:
        break


while len(arr) > 0 :
    del arr[len(arr)-1]
    print arr

