# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
 
# set width of bar
barWidth = 0.35

fig, ax = plt.subplots()
ax.set(ylim=[-4.5, 20])


formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
ax.yaxis.set_major_formatter(formatter)
 
# set height of bar
bars1 = [0, 0, 0, 0, 0, 0, 0]

# overhead
bars2 = [8.2, 7.8, 7.5, 7.3, 6.1, 10.3, 9.1]
err = (2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) 
 

# offset
bars1 = [x + 4 for x in bars1] 
bars2 = [x + 4 for x in bars2] 


# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='w', width=barWidth, edgecolor='#7f6d5f', bottom=-4, hatch='#', label='None')
plt.bar(r2, bars2, yerr=err, color='#7f6d5f', width=barWidth, edgecolor='#557f2d', bottom=-4, hatch='#', label='Mitigation')
 
# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['nginx', 'apache', 'sqlite3', '7z', 'zlib', 'serv-u', 'coreftp'])
plt.xticks(rotation =50,fontsize =8)
 

# Create legend & Show graphic
plt.legend()
plt.show()

