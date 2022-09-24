keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
x = dict()
for i in range(len(keys)):
    x.update({keys[i]: values[i]})
print(x)