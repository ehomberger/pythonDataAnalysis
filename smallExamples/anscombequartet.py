import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="ticks")

# load example data set
df = sns.load_dataset("anscombe")

# show the results of linear regression
sns.lmplot(x = 'x', y = 'y', col = "dataset", hue = "dataset", data = df,
            col_wrap = 2, ci = None, palette = "muted", size = 4,
            scatter_kws={'s': 50, "alpha": 1})

plt.show()
