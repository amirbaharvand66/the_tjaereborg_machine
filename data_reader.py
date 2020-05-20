import numpy as np


class airfoil():
    def __init__(self):
        self.alpha = []
        self.cl = []
        self.cd = []

    def airfoil_reader(self, self_in_str: str):
        airfoil_id = 'data\\' + self_in_str + '.dat'
        self.airfoil_data = np.genfromtxt(airfoil_id)
        for row in range(len(self.airfoil_data)):
            self.alpha.append(self.airfoil_data[row][0])
            self.cl.append(self.airfoil_data[row][1])
            self.cd.append(self.airfoil_data[row][2])
        return np.array(self.alpha), np.array(self.cl), np.array(self.cd)

airfoil_names = []
tjaere04 = airfoil()
tjaere05 = airfoil()
tjaere06 = airfoil()
tjaere07 = airfoil()
tjaere08 = airfoil()
tjaere09 = airfoil()
tjaere10 = airfoil()
tjaere11 = airfoil()
tjaere12 = airfoil()
tjaere13 = airfoil()
tjaere14 = airfoil()
tjaere04.airfoil_reader('tjaere04')
tjaere05.airfoil_reader('tjaere05')
tjaere06.airfoil_reader('tjaere06')
tjaere07.airfoil_reader('tjaere07')
tjaere08.airfoil_reader('tjaere08')
tjaere09.airfoil_reader('tjaere09')
tjaere10.airfoil_reader('tjaere10')
tjaere11.airfoil_reader('tjaere11')
tjaere12.airfoil_reader('tjaere12')
tjaere13.airfoil_reader('tjaere13')
tjaere14.airfoil_reader('tjaere14')


