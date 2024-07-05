import pandas as pd
import dash
from dash import Dash, dcc, html
import matplotlib.pyplot as plt
import plotly.express as px

#read dataframe
games = pd.read_csv('/Users/ayeshajan/Desktop/Video-Games-And-The-Male-Gaze/data/games_clean.grivg.csv')
characters = pd.read_csv('/Users/ayeshajan/Desktop/Video-Games-And-The-Male-Gaze/data/characters_clean.grivg.csv')
developers = pd.read_csv('/Users/ayeshajan/Desktop/Video-Games-And-The-Male-Gaze/data/cleaned_video_game_developers_worldwide2014_2021.csv')
developers_women = developers[developers['gender'] == 'women']
developers_men = developers[developers['gender'] == 'men']
developers_non_binary = developers[developers['gender'] == 'non-binary']

#create the figures and define them
fig1 = px.bar(games, x = "game_id", y= ["male_team","female_team"], title="Amount of Female vs Male Developers in The Team")
fig2 = px.bar(games, x = "game_id", y= ["protagonist_male","protagonist_non_male"], title="Amount of Male vs Non-Male Protagonists")
fig3 = px.line(games, x = games["release"], y = games["female_team_percentage_per_date"], title = "Female Team Percentage From 2012-2022")

fig4 = px.bar(characters, x = 'gender', y = 'sexualization', title = "The Amount of Sexualization Per Gender")

fig5 = px.line(developers_women, x = developers_women["year"], y = developers_women["percentage"], title = 'Percentage of Female Developers Worldwide Between 2014-2021')
fig5.update_layout(yaxis_range=[0,100])
fig6 = px.line(developers_women, x = developers_women["year"], y = developers_women["percentage"], title = 'Percentage of Male vs Female vs Non-Binary Developers Worldwide Between 2014-2021')
fig6.add_scatter(x =developers_men['year'], y = developers_men['percentage'], name = "Male")
fig6.add_scatter(x =developers_non_binary['year'], y = developers_non_binary['percentage'], name = "Non-Binary")
fig6.update_layout(yaxis_range=[0,100])

#creating dcc components
graph1 = dcc.Graph(figure=fig1)
graph2 = dcc.Graph(figure=fig2)
graph3 = dcc.Graph(figure=fig3) 
graph4 = dcc.Graph(figure=fig4) 
graph5 = dcc.Graph(figure=fig5) 
graph6 = dcc.Graph(figure=fig6) 

app =dash.Dash()
app.layout = html.Div([html.H1('Gender Disparity Within The Gaming Community', style={'textAlign': 'center', 'color': '#636EFA'}), 
                       graph1, 
                       graph2,
                       graph3,
                       graph4,
                       graph5,
                       graph6, 
                       
])

 
if __name__ == '__main__':
     app.run_server()