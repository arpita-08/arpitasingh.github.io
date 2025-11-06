list1 = [1,2,3,4,3,1,5,4]

s = set(list1)
s.add(1)
s.add(2)

s = list(s)

s = list(map(lambda val: val*5, s))

s.remove(5)
s.add(5)

print(s)