#######################################################
#     Last Revision: 03/07/2021                       #
#     Python Version:  3.9                            #
#     Email: Daskalakispiros@gmail.com                #
#######################################################

import numpy as np
import matplotlib.pyplot as plt  #for plotting the data
import scipy.io


mat = scipy.io.loadmat('V_I_A301A_1.mat')
V_reading_1 = np.array(mat['v_reading']) [0]
i_reading_1 = np.array(mat['i_reading']) [0]

mat = scipy.io.loadmat('V_I_A301A_2.mat')
V_reading_2 = np.array(mat['v_reading']) [0]
i_reading_2 = np.array(mat['i_reading']) [0]

mat = scipy.io.loadmat('V_I_A301A_3.mat')
V_reading_3 = np.array(mat['v_reading']) [0]
i_reading_3 = np.array(mat['i_reading']) [0]


mat = scipy.io.loadmat('V_I_A301A_4.mat')
V_reading_4 = np.array(mat['v_reading']) [0]
i_reading_4 = np.array(mat['i_reading']) [0]


fig1 = plt.figure()
plt.rcParams['font.size'] = 18
plt.rcParams['font.sans-serif'] ="Arial"
plt.plot(V_reading_1, i_reading_1,'-o', label='Diode 1', linewidth=1.5)
plt.plot(V_reading_2, i_reading_2, label='Diode 2', linewidth=1.5)
plt.plot(V_reading_3, i_reading_3, label='Diode 3', linewidth=1.5)
plt.plot(V_reading_4, i_reading_4, label='Diode 4', linewidth=1.5)

plt.xlabel('Millivolt (mV)')
plt.ylabel('Current (mA)')
plt.title('I V curves')
plt.legend()
plt.grid()
plt.savefig('My_diode_model.png', dpi=300, transparent=False)
plt.show()