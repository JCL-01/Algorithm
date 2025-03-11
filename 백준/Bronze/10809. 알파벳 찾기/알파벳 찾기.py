string = input()
ord_num = 97
site_list = []
for i in range(26):
    if chr(ord_num + i) in string:
        site_list.append(string.find(chr(ord_num + i)))
    else: 
        site_list.append(-1)
print(*site_list)
