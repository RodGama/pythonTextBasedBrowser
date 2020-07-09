row = int(input())
coluna = int(input())
count = 0
if row == 1 or row == 8:
    if coluna == 1 or coluna == 8:
        count = 3
    else:
        count = 5
else:
    if coluna == 1 or coluna == 8:
        count = 5
    else:
        count = 8

print(count)
