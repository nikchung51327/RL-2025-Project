# E1,2
from math import pi


L1 = [10, 20, 30, 40, 50, 60]
print(L1[0], L1[-1])
print(L1[1:4])

#E3
L2 = ['Hi', 'Hello', 'Hi!', 'Hey', 'Hi', 'hey', 'Hey']
L2 = list(set(L2))
print(L2)

#E4
d = {2: 122, 3: 535, 't': 'T', 'rum': 'cola'}
for keys in d:
    print(d[keys])

#E5
n = [23, 73, 12, 84]
for num in n:
    num_sq = num**2
    print(f'{num} sqaured is {num_sq}')

#E6
diameters = [10, 12, 16, 20, 25, 32]
circle_area = [round(pi*((diameter)/2)**2,2) for diameter in diameters]
print(circle_area)

#E7
phonetic_alphabet = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
list_5 = [name for name in phonetic_alphabet if len(name) == 5]
print(list_5)

#E8
s1 = {'HE170B', 'HE210B', 'HE190A', 'HE200A', 'HE210A', 'HE210A'}

s2 = {'HE200A', 'HE210A', 'HE240A', 'HE200A', 'HE210B', 'HE340A'}

print(s1.intersection(s2))

#E9

fy = 435
rebar_stresses = (125, 501, 362, 156, 80, 475, 489)
fy_list = []

for stresses in rebar_stresses:
    if stresses < fy:
        fy_list.append(stresses)
    else:
        fy_list.append(fy)

print(fy_list)

#E10
T1 = (-18, -27, 2, -21, -15, 5)
t1_list = []

for num in T1:
    if num > 0:
        t1_list.append(0)

    elif num < -25:
        t1_list.append(-25)
    
    else:
        t1_list.append(num)

print(t1_list)