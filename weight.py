import pandas as pd
import plotly.figure_factory as pff
df  = pd.read_csv('data.csv')
weight = df['Weight(Pounds)'].tolist()
graph = pff.create_distplot([weight], ['Weight'], show_hist=False )
graph.show()