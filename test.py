codes=[1,2,3]
names=['aa','bb','cc']
d={}
for x in range(len(codes)):
    d[codes[x]]=names[x]
print(x)
d[4]='ee'
print("dictionary extended")
print(d)
d.update({2:'bd'})
print("dictinary updated")
print(d)
print("remove element",2,":",d.pop(2))
print("after removing 2 element")
print(d)
