strlist = ["","",""]


for i in range(len(strlist)):
    strlist[i] = raw_input("Enter:")

c = strlist[0]
strlist[0] = strlist[2]
strlist[2] = c
strlist[1] = [1,2,3]
print strlist[1][1]