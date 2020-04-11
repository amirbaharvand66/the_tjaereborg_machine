tjaere04 = []
with open('tjaere04.dat', 'r') as air_foil_1:
    for line in air_foil_1:
        tjaere04.append(line.strip())


tjaere04_l_1 = []
alpha = []
for item in range(len(tjaere04)):
    tjaere04_l_1 = tjaere04[item].split('     ')
    alpha.append(tjaere04_l_1[0])

alpha = list(map(float, alpha))

tjaere04_l_1 = []
C_l = []
for item in range(len(tjaere04)):
    tjaere04_l_1 = tjaere04[item].split('     ')
    C_l.append(tjaere04_l_1[1])

C_l = list(map(float, C_l))

tjaere04_l_1 = []
C_d = []
for item in range(len(tjaere04)):
    tjaere04_l_1 = tjaere04[item].split('     ')
    C_d.append(tjaere04_l_1[2])

C_d = list(map(float, C_d))
