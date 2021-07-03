#######################################################
#     Author: Spyros Daskalakis                       #
#     Last Revision: 03/07/2021                       #
#     Python Version:  3.9                            #
#     Email: Daskalakispiros@gmail.com                #
#######################################################


import numpy as np
import matplotlib.pyplot as plt  # for plotting the data
import scipy.io

# My Data
mat = scipy.io.loadmat('V_I_A301A_3.mat')
V_reading_3 = np.array(mat['v_reading'])[0]
i_reading_3 = np.array(mat['i_reading'])[0]

# paper function
V_paper = np.arange(0, 0.7, 0.01)
I_paper = -5.83 * (V_paper ** 7) + 14.12 * (V_paper ** 6) - 12.87 * (V_paper ** 5) + 5.10 * (V_paper ** 4) - 0.53 * (
            V_paper ** 3) - 0.18 * (V_paper ** 2) + 0.04 * V_paper - 1.47 * 10 ** (-5)

# polyfit
z = np.polyfit(V_reading_3, i_reading_3, 12)
p = np.poly1d(z)
print(p)

fig1 = plt.figure()
plt.rcParams['font.size'] = 18
plt.rcParams['font.sans-serif'] = "Arial"
plt.plot(V_reading_3, i_reading_3,'-o', label='My Data, Diode 3', linewidth=1.5)
plt.plot(V_reading_3, p(V_reading_3), label='Curve fitting Diode 3', linewidth=1.5)
plt.plot(V_paper * 1000, I_paper * 1000, label='S. Hemour Et al.', linewidth=1.5)
plt.xlabel('Millivolt (mV)')
plt.ylabel('Current (mA)')
plt.title('I V curves')
plt.legend()
plt.grid()
plt.savefig('My_diode_model.png', dpi=300, transparent=False)
plt.show()

