from pylab import *
import matplotlib.patches as patches

#Imaging resolution for the four bands as a function of spacecraft distance to the target body


'''
VIS
10 x 10 FOV
1024 x 1024 pixels

NIR-1
6.7 x 5.4 FOV
640 x 512 pixels

NIR-2
6.7 x 5.4 FOV
640 x 512 pixels

SWIR
5 circular
1 pixel


'''

#Spacecraft distance to the TCO (m)
d = logspace(2, 6, 100)

#For VIS
aVIS = 10*pi/180
pxVIS = 1024
pVIS = d*tan(aVIS/(2*pxVIS))

#For NIR-1 and NIR-2

aNIR1 = 6.7*pi/180
aNIR2 = 5.4*pi/180
pxNIR1 = 640
pxNIR2 = 512

pNIR1 = 2*d*tan(aNIR1/(pxNIR1*2))
pNIR2 = 2*d*tan(aNIR2/(pxNIR2*2))


#Hera Milani numbers for validation - TBD

#Size of the TCO
fig, ax = plt.subplots()
ax.plot(d/1e3, pVIS, 'k')
ax.plot(d/1e3, pNIR1, 'k-.')
ax.plot(d/1e3, pNIR2, 'k--')
ax.plot(d/1e3, tan(aVIS/2)*d*2, 'b')
ax.plot(d/1e3, tan(aNIR1/2)*d*2, 'b-.')
ax.plot(d/1e3, tan(aNIR2/2)*d*2, 'b--')
rectangle =  patches.Rectangle((1, 1), 1000, 100, edgecolor='red', facecolor='red', linewidth=1, alpha = 0.3)
ax.add_patch(rectangle)
grid()
#xscale('log')
ax.set_yscale('log')
ax.legend(['VIS resolution', 'NIR 1 and NIR 2 - x resolution', 'NIR 1 and NIR 2 - y resolution', 'VIS FOV', 'NIR 1 and NIR 2 - x FOV', 'NIR 1 and NIR 2 - y FOV'], loc = 'best')
ax.set_xlabel('Distance from the target (km)')
ax.set_ylabel('Image resolution (m/px) and FOV (m)')
show()
#savefig('../../Resolution.png')
