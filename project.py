import pandas
import plotly.express as px

df = pandas.read_csv("data.csv")
df_2 = df.groupby(["student_id", "level"],as_index = False)["attempt"].mean()

fig = px.scatter(df_2,x = "student_id", y = "level", size = "attempt", color= "attempt")
fig.show()
