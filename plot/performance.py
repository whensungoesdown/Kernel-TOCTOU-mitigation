import numpy as np
import matplotlib.pyplot as plt


N = 7 
standard = (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
overhead = (0.032, 0.028, 0.025, 0.023, 0.011, 0.053, 0.041)
err = (0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005) 
ind = np.arange(N)    # the x locations for the groups
width = 0.55       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, standard, width, edgecolor='blue')
p2 = plt.bar(ind, overhead, width,
                     bottom=standard, yerr=err, color=(0.2, 0.4, 0.6, 0.6),  edgecolor='blue')

plt.ylabel('Performance Overhead')
#plt.title('Scores by group and gender')
plt.xticks(ind, ('nginx', 'apache', 'sqlite3', '7z', 'zlib', 'serv-u', 'coreftp'))
plt.yticks(np.arange(0, 1.2, 0.01))
plt.gca().set_yticklabels(['{:.00f}%'.format(x*100) for x in plt.gca().get_yticks()])
plt.ylim(0.99, 1.06)
plt.legend((p1[0], p2[0]), ('w/o mitigation', 'w/ mitigation'))


plt.tight_layout()
plt.show()
