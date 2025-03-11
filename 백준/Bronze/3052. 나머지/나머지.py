remainder_list = []
for i in range(10):
    remainder = int(input())%42
    if remainder not in remainder_list:
        remainder_list.append(remainder)
print(len(remainder_list))