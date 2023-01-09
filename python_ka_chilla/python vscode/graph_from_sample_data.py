import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import data from file
df = pd.read_csv("python vscode/sample_data.csv")
sns.set_theme(style="ticks", color_codes=True)

p = sns.countplot(x="Gender", hue="Sick_Days_remaining", data=df)
plt.title("Sample Data Graph")
plt.show()


# there are two ways to set title of a graph
# 1 - plt.title("Sample Data Graph")
# 2 - p.set_title("Sample Data Graph")