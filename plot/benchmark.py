# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
 
# set width of bar
barWidth = 0.25

fig, ax = plt.subplots()
ax.set(ylim=[-4.3, 12])


formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
ax.yaxis.set_major_formatter(formatter)
 
# set height of bar
bars1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bars2 = [0, 10.0, 0.3, 1.4, 2.3, -0.6, 10.8, 3.1, 0, -1.8, 4.2]
bars3 = [0, 2.0, 0.3, 1.4, 1.0, 0.3, 2.0, 3.5, 0, -1.9, 1.8]
 

# offset
bars1 = [x + 4 for x in bars1] 
bars2 = [x + 4 for x in bars2] 
bars3 = [x + 4 for x in bars3] 


# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
plt.bar(r1, bars1, color='w', width=barWidth, edgecolor='#7f6d5f', bottom=-4, hatch='#', label='None')
plt.bar(r2, bars2, color='#7f6d5f', width=barWidth, edgecolor='#557f2d', bottom=-4, hatch='#', label='Hypervisor')
plt.bar(r3, bars3, color='w', width=barWidth, edgecolor='#2d7f5e', bottom=-4, hatch='///', label='HVCI')
 
# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['bzip2', 'mcf', 'gobmk', 'hnner', 'sjeng', 'h264ref', 'omnetpp', 'milc', 'namd', 'lbm', 'sphinx3'])
plt.xticks(rotation =50,fontsize =8)
 

# Create legend & Show graphic
plt.legend()
plt.show()

