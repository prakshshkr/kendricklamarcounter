from matplotlib import pyplot as plt
d = {}
with open("newcount.txt") as f:
    for line in f:
    	(key, val)=line.split()[::-1]
    	d[key] = int(val)
keys = d.keys()
values = d.values()
plt.title('Kendrick Lamar\'s 100 most used words')
plt.bar(keys, values,align='edge', width=0.6)
plt.xticks(rotation=90,fontsize=10)
plt.show()
