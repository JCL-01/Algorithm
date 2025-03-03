list = input().split(' ')
if int(list[0]) > int(list[1]):
    print('>')
elif int(list[0]) == int(list[1]):
    print('==')
elif int(list[0]) < int(list[1]):
    print('<')