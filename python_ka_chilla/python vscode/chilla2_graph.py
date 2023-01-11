import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

mydata = pd.read_csv("python vscode/chilla2_dataset.csv")



# using sample data in different plots
# 1 - Sunburst Plot 
fig = px.sunburst(mydata, path=['Qualification_completed', 'field_of_study'], values='How many hours you code a day? (int) e.g: 5,4,3',
                  color='Age (years)-Float/Int', hover_data=['Location', 'Gender'])
fig.show()


# 2 - Countplot
sns.countplot(x="Qualification_completed", hue="Gender", data=mydata)
plt.show()

