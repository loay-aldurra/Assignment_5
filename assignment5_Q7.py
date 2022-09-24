set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
for i in set1:
    for j in set2:
        if i == j:
            set3.add(i)
print(set3)