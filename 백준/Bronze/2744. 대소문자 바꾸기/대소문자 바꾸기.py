org_str = input()
new_str = ''
for letter in org_str:
    if ord(letter) < 97:
        new_str += chr(ord(letter)+32)
    else:
        new_str += chr(ord(letter)-32)
print(new_str)
