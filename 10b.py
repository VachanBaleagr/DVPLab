
import pandas as pd
import plotly.express as px
data=pd.read_csv('gapminder_with_codes.csv')
fig=px.choropleth(data,locations='iso_alpha',color='gdpPercap',hover_name='country',
                  projection='natural earth',title='GDP per Capita by country-Vachan-1KI23CS173')
fig.show()