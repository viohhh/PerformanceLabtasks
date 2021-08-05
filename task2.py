import sys

f1 = sys.argv[1]
f2 = sys.argv[2]
file1 = open(f1, 'r')
file2 = open(f2, 'r')

l = [line.strip() for line in file1]

rx, ry = l[0].split()
rx = int(rx)
ry = int(ry)
r = int(l[1])

l = [line.strip() for line in file2]

dots = []

for i in l:
    dots.append([int(x) for x in i.split()])

for i in dots:
    s = pow((i[0] - rx), 2) + pow((i[1] - ry), 2)
    s = pow(s, 0.5)

    if s < r:
        print('1')
    elif s == r:
        print('0')
    else:
        print('2')