string = input()
ord_num = 97
site_list = []
for i in range(26):
    if chr(ord_num + i) in string:
        site_list.append(string.find(chr(ord_num + i)))
    else: 
        site_list.append(-1)
print(
    site_list[0],
    site_list[1],
    site_list[2],
    site_list[3],
    site_list[4],
    site_list[5],
    site_list[6],
    site_list[7],
    site_list[8],
    site_list[9],
    site_list[10],
    site_list[11],
    site_list[12],
    site_list[13],
    site_list[14],
    site_list[15],
    site_list[16],
    site_list[17],
    site_list[18],
    site_list[19],
    site_list[20],
    site_list[21],
    site_list[22],
    site_list[23],
    site_list[24],
    site_list[25]
)
