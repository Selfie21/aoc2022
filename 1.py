p1 = None
p2 = None
aggr = 0
new = []

for line in open('1.in', "r"):
    line = line.strip()
    if line == '':
        new.append(aggr)
        aggr = 0
    else:
        aggr += int(line)

p1 = max(new)
new.sort()
p2 = new[-1] + new[-2] + new[-3]
print(p1)
print(p2)
