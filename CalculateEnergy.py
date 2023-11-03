#from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt
#from sympy import integrate, init_printing
import pandas as pd
def Get_Energy(path):
    #path = 'Tabla_Monofasica.xlsx'
    data = pd.read_excel(path, header=None)
    x = []
    y = []
    fi = []

    Tiempo = 0
    t = 1
    a = 0
    Vmax = 0
    Energy = 0
    Energy2 = 0
    for i in data[0]:
        a = a + t
        # if a % 10 == 0:
        x.append(a)
        y.append(i*i)
        if i > Vmax:
            Vmax = i
        elif Vmax != 0 and i <= Vmax*0.5 and Tiempo == 0:
            Tiempo = a
            print(i)

        try:
            Energy2 = Energy2+t*(y[-2])
            if y[-1] > y[-2]:
                Energy = Energy+t*(y[-2])+t*(abs(y[-2]-y[-1])/2)
            else:
                Energy = Energy+t*(y[-1])+t*(abs(y[-2]-y[-1])/2)
            fi.append(Energy/25)
        except:
            fi.append(0)
            pass
    return Energy

#if __name__ == "__main__":
    
    #EnergyError = abs(Energy-Energy2)


    #print(Energy, Energy2, EnergyError, Vmax, Tiempo)
#x = [0, 1, 3, 6]
#y = [-3, 0, 5, 7]
#p = lagrange(x, y)

#x1 = np.linspace(0, 100, 100)
#y1 = p(x1)

#plt.plot(x1, y1, label='interpolacion')
#plt.plot(x, y, label="datos")
#plt.plot(x, fi, label="integral")
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
#plt.show()

print('finalizado')
# print(integrate(p))
