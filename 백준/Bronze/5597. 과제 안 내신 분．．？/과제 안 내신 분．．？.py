attendants = []
for _ in range(28):
    attendants.append(int(input()))

absentee = []
for i in range(1, 31):
    if i in attendants:
        continue
    else:
        absentee.append(i)
absentee.sort()
print(absentee[0], absentee[1], sep='\n')