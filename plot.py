import pandas as pd
import plotly.express as px
from io import StringIO

# Your data
data = """
Technology, date, intelligence, generativeness
Checkers, 1960, 0, 0
Atari Games AI, 1978, 2, 3
Stanford Cart, 1979, 5, 3
Expert Systems, 1983, 10, 4
Autonomous drawing program, 1985, 7, 10
TD-Gammon, 1992, 13, 7
Deep Blue, 1997, 17, 8
Furby, 1999, 4, 4
Spirit and Opportunity rovers, 2004, 25, 9
Google autonomous car, 2009, 28, 9
Watson and Jeopardy!, 2011, 32, 17
Apple Siri, 2011, 20, 12
Google Now, 2012, 20, 12
Cortana, 2014, 20, 12
AlphaGo, 2016, 40, 15
GPT-1, 2018, 43, 35
AlphaStar, 2019, 43, 20
GPT-2, 2019, 47, 40
GPT-3, 2020, 51, 45
GPT-3.5, 2022, 65, 70
GPT-4, 2023, 75, 80
Meta Llama, 2023, 75, 80
Google Bard, 2023, 75, 80
"""




# Load the data into a pandas DataFrame
df = pd.read_csv(StringIO(data))
df.columns = df.columns.str.strip()

data_1960 = df.filter(regex='196$')

# Create animated bubble chart
fig = px.scatter(df, 
                 x="intelligence", 
                 y="generativeness", 
                 animation_frame="date", 
                 animation_group="Technology", 
                 size=df["intelligence"] + df["generativeness"], 
                 hover_name="Technology", 
                 size_max=60, 
                 range_x=[-5, 80], 
                 range_y=[-5, 85], 
                 labels={"intelligence": "Intelligence", "generativeness": "Generativeness"},
                 title="Technologies Over Time Based on Intelligence and Generativeness")

# Show the plot
#fig.show()

print(data_1960)