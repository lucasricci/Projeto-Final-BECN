import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("BECN.csv")

# df.loc[df.banana == "Amanda", "grau"] = 1
# df.loc[df.banana == "Otavia", "grau"] = 1
# df.loc[df.banana == "Betania", "grau"] = 1


# sns.lmplot(x="r", y="resistividade", data=df)
# sns.lmplot(x="g", y="resistividade", data=df)
# sns.lmplot(x="b", y="resistividade", data=df)

plt.figure(dpi=160)
sns.lineplot(
    x="tempo",
    y="resistencia",
    hue="grau",
    data=df,
)
plt.show()
