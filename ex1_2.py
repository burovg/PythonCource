s1 = raw_input("First string: ")
s2 = raw_input("Seconf string: ")
num = input("Number: ")
ls = ""
sms = ""
count = 0

if s1 > s2:
    print "Larger " + s1
    ls = s1
    sms = s2
else:
    print "Larger " + s2
    ls = s2
    sms = s1
if s1 in s2:
    print s1 + " is in " + s2
else:
    print s2 + " is in " + s1
s3 = ls[0:num]
c = str(sms[num])
ls = ls.replace(c,"Gershon")


ts = ls + sms + s3
for ch in ts:
    if ch == "A" :
        count = count +1
print count







