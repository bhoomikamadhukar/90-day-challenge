import re
for _ in range(int(input())):
    number=input()
    match=re.match(r"^[789](\d){9}$",number)
    if match:
        print('YES')
    else:
        print('NO')