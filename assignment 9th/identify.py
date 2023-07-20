x = ["kabul", "panjisher", "baghlan"]
y = ["kabul", "panjisher", "baghlan"]
d = x
print(d is x)
print( d == y)


class1 = ["suhrab", 'kabir', "zekria", "taher"]
class2 = ["suhrab", 'kabir', "zekria", "taher"]
class3 = class1
print(class3 is not class2)
print(class3 is not class1)