# Code écrit par Clem et George

import re
import matplotlib.pyplot as plt

def sum_meilleur(tab):
    sum = 0
    temp=[]
    for i in tab:
        sum+=i
        temp.append(sum)
    return temp


f = open("data.txt", "r")
d = f.read()
f.close()

tab=[]
for match in re.finditer(r"[^;]+;[^S]+S(\d)+\";[^;]+;(\d+)", d):
            tab.append(int(match.group(2)))

plt.plot(sum_meilleur(tab))
plt.savefig("fig.png")
