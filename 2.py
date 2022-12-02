p1 = None
p2 = None

dict1 = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

dict2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
mappingswin = {
    'A X': 'Z',
    'A Y': 'X',
    'A Z': 'Y',
    'B X': 'X',
    'B Y': 'Y',
    'B Z': 'Z',
    'C X': 'Y',
    'C Y': 'Z',
    'C Z': 'X'
}

winconds = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3
}

aggr = 0
for line in open('2.in', "r"):
    line = line.strip()
    me = line[2]
    p1 += dict1[me]
    p1 += winconds[line]

    wins = line[2]
    p2 += dict2[wins]
    p2 += dict1[mappingswin[line]]
print(p1)
print(p2)
