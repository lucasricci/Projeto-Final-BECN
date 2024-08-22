import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("BECN.csv")
maturity = ["#00FF00", "#7FFF00", "#BFFF00", "#DFFF00", "#FFFF00"]

plt.figure(dpi=160)
sns.lineplot(x="tempo", y="resistencia", hue="grau", data=df, palette="bright")
plt.show()
