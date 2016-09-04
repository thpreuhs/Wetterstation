import CreatePolarPlot as cpp
import math
import numpy as np
import matplotlib.pyplot as plt

data = cpp.generate_Data()
data = data[:-1] # this is now percent


res = 0
for date in data:
    res += date

print(res)

#values, azimuths, zeniths
degree = [] # degree
for i in range(0,16):
    degree.append(i*22.5*math.pi/180)

zeniths = data



ax = plt.subplot(111, projection='polar')
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
#ax.contourf(degree, data, 30)
ax.plot(degree, data, color='r', linewidth=3)
ax.set_rmax(max(data))
ax.grid(True)
#ticklocs = ax.xaxis.get_ticklocs()
#ax.xaxis.set_ticklabels([chr(number + 65) for number in range(len(ticklocs))])

ax.set_xticks(degree)
#ax.xaxis.set_ticklabels([chr(number + 65) for number in range(len(degree))])
ax.xaxis.set_ticklabels(['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'])
ax.set_title("Windrose", va='bottom')
plt.show()
