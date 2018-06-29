import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

# plt.style.use('default')

df = pd.read_csv("../2016-2018_florida_zika_travel_cases.csv")
df = df.set_index("year")
df = df.drop("Month")
df = df.drop("Total", axis = 1)

_s = int(len(df.index) ** 0.5)
plt.figure(figsize=(15, 17))
g = gs.GridSpec(_s+1, _s-1)

for i in range(0, _s+1):
    for j in range(0, _s-1):
        ax = plt.subplot(g[i,j])
        c = df.index[(i * (_s-1) + j)]
        ax.plot(df.columns.astype(float).sort_values(), df.ix[c].astype(float).tolist(), color='steelblue')
        ax.set_title(c)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.fill_between(df.columns.astype(float).sort_values(), 0, df.ix[c].astype(float).tolist(), facecolor="steelblue", alpha = 0.4)

plt.tight_layout()
plt.savefig("../plots/travel.png")
plt.clf()
plt.close()
