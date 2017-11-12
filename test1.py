sum = 0
b = True

while b == True :
    a = int(raw_input("Enter number: "))
    sum = sum + a
    if sum > 30 :
        b = False
        print "End of loop"
print sum
