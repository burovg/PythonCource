
names = ["Dov","Ronen","Dana","Forever"]

a = filter(lambda x: len(x) > 3,names)
print a

b = map(lambda x:len(x) > 3,names)
print b