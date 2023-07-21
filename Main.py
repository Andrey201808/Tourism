from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/AttractivePoints13.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/AttractivePoints13.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/AdditionalPoints7.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/Cafe.csv')
df5 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/CafeDevelopment.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/DivByTypes.csv')
df7 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/KRC_Arh.csv')
df8 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/KSRDevelopment.csv')
df9 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/PackageTours.csv')
df10 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/RoadsDevelopment.csv')
df11 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/Routes.csv')
df12 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/TouristsPoints.csv')
df13 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/TouristsTypes.csv')
df14 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/Transport.csv')
df15 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/TransportDevelopment.csv')
df16 = pd.read_csv('https://raw.githubusercontent.com/Andrey201808/Tourism/main/Turpotok.csv')
app = Dash(__name__)



app.layout = (

    html.Div([html.Div
              ([
    html.H1(children='Основные точки привлечения туристов', style={'textAlign':'center'}),
    dcc.Dropdown(df.PointName.unique(), 'Архангельский театр драмы имени М.В. Ломоносова', id='dropdown-selection'),
    dcc.Graph(id='graph-content',figure=px.histogram(df, x='DaysMax', y='TouristsCount')),
    
    html.H1(children='Основные точки привлечения туристов', style={'textAlign':'center'}),
    dcc.Dropdown(df2.PointName.unique(), 'Архангельский театр драмы имени М.В. Ломоносова', id='dropdown-selection2'),
    dcc.Graph(id='graph-content2',figure=px.histogram(df2, x='TouristsCount', y='AvPointPrice')),


    html.H1(children='Дополнительные точки привлечения туристов', style={'textAlign':'center'}),
    dcc.Dropdown(df3.PointName.unique(), 'Национальный туристкий маршрут «Архангельск: здесь начинается Арктика»', id='dropdown-selection3'),
    dcc.Graph(id='graph-content3',figure=px.histogram(df3, x='PointTime', y='OrderDay')),
    
    html.H1(children='Заведения общественного питания', style={'textAlign':'center'}),
    dcc.Dropdown(df4.Name.unique(), '«Рандеву»', id='dropdown-selection4'),
    dcc.Graph(id='graph-content4',figure=px.histogram(df4, x='Tourists', y='AvPrice')),

    html.H1(children='Развитие заведений общественного питания', style={'textAlign':'center'}),
    dcc.Dropdown(df5.Name.unique(), '«Мечта»', id='dropdown-selection5'),
    dcc.Graph(id='graph-content5',figure=px.histogram(df5, x='Tourists', y='PlanCost')),

    
    html.H1(children='Виды туризма', style={'textAlign':'center'}),
    dcc.Dropdown(df6.TourismType.unique(), 'Круизный', id='dropdown-selection6'),
    dcc.Graph(id='graph-content6',figure=px.histogram(df6, x='PartOfCommon', y='TripDays')),

    
    html.H1(children='Места отдыха', style={'textAlign':'center'}),
    dcc.Dropdown(df7.ObjectName.unique(), 'Гостиница «Двина»', id='dropdown-selection7'),
    dcc.Graph(id='graph-content7',figure=px.histogram(df7, x='FirstNum', y='FirstPlace')),

    
    html.H1(children='Развитие мест отдыха', style={'textAlign':'center'}),
    dcc.Dropdown(df8.Location.unique(), 'Точка привлечениия1', id='dropdown-selection8'),
    dcc.Graph(id='graph-content8',figure=px.histogram(df8, x='Tourist', y='AvCost')),

    
    html.H1(children='Пакетные туры', style={'textAlign':'center'}),
    dcc.Dropdown(df9.TourName.unique(), 'Знакомство с Северным Байкалом', id='dropdown-selection9'),
    dcc.Graph(id='graph-content9',figure=px.histogram(df9, x='TourDay', y='TouristsCount')),

    
    html.H1(children='Развитие дорог', style={'textAlign':'center'}),
    dcc.Dropdown(df10.RouteType.unique(), 'автомобильная дорога', id='dropdown-selection10'),
    dcc.Graph(id='graph-content10',figure=px.histogram(df10, x='AvDaysClosed', y='TransportsThread')),

    
    html.H1(children='Маршруты', style={'textAlign':'center'}),
    dcc.Dropdown(df11.RouteType.unique(), 'автомобильная дорога', id='dropdown-selection11'),
    dcc.Graph(id='graph-content11',figure=px.histogram(df11, x='AvDaysClosed', y='TransportThread')),

    
    html.H1(children='Туристические объекты', style={'textAlign':'center'}),
    dcc.Dropdown(df12.PointName.unique(), 'Архангельский театр драмы имени М.В. Ломоносова', id='dropdown-selection12'),
    dcc.Graph(id='graph-content12',figure=px.histogram(df12, x='MaxDays', y='MinDays')),

    
    html.H1(children='Типы туризма', style={'textAlign':'center'}),
    dcc.Dropdown(df13.TourismType.unique(), 'Круизный', id='dropdown-selection13'),
    dcc.Graph(id='graph-content13',figure=px.histogram(df13, x='AvDaysTrip', y='AvCostTrip')),

    
    html.H1(children='Транспорт', style={'textAlign':'center'}),
    dcc.Dropdown(df14.TransportNodeName.unique(), 'Речной вокзал', id='dropdown-selection14'),
    dcc.Graph(id='graph-content14',figure=px.histogram(df14, x='TouristsThread', y='TransportThread')),

    
    html.H1(children='Развитие транспорта', style={'textAlign':'center'}),
    dcc.Dropdown(df15.TransportNodeName.unique(), 'Речной вокзал', id='dropdown-selection15'),
    dcc.Graph(id='graph-content15',figure=px.histogram(df15, x='TouristsThread', y='TransportThread')),

    
    html.H1(children='Туристический поток', style={'textAlign':'center'}),
    dcc.Dropdown(df16.Year.unique(), '2022', id='dropdown-selection16'),
    dcc.Graph(id='graph-content16',figure=px.histogram(df16, x='Year', y='December')),
    
            ]),
              ])
             
    )

@callback(
    Output('graph-content', 'figure'),
    Output('graph-content2', 'figure'),
    Output('graph-content3', 'figure'),
    Output('graph-content4', 'figure'),
    Output('graph-content5', 'figure'),
    Output('graph-content6', 'figure'),
    Output('graph-content7', 'figure'),
    Output('graph-content8', 'figure'),
    Output('graph-content9', 'figure'),
    Output('graph-content10', 'figure'),
    Output('graph-content11', 'figure'),
    Output('graph-content12', 'figure'),
    Output('graph-content13', 'figure'),
    Output('graph-content14', 'figure'),
    Output('graph-content15', 'figure'),
    Output('graph-content16', 'figure'),
    Input('dropdown-selection', 'value'),
    Input('dropdown-selection2', 'value'),
    Input('dropdown-selection3', 'value'),
    Input('dropdown-selection4', 'value'),
    Input('dropdown-selection5', 'value'),
    Input('dropdown-selection6', 'value'),
    Input('dropdown-selection7', 'value'),
    Input('dropdown-selection8', 'value'),
    Input('dropdown-selection9', 'value'),
    Input('dropdown-selection10', 'value'),
    Input('dropdown-selection11', 'value'),
    Input('dropdown-selection12', 'value'),
    Input('dropdown-selection13', 'value'),
    Input('dropdown-selection14', 'value'),
    Input('dropdown-selection15', 'value'),
    Input('dropdown-selection16', 'value')
)

def update_graph(value,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,value11,value12,value13,value14,value15):
    dff = df[df.PointName==value]
    dff2 = df2[df2.PointName==value1]
    dff3 = df3[df3.PointName==value2]
    dff4 = df4[df4.Name==value3]
    dff5 = df5[df5.Name==value4]
    dff6 = df6[df6.TourismType==value5]
    dff7 = df7[df7.ObjectName==value6]
    dff8=df8[df8.Location==value7]
    dff9 = df9[df9.TourName==value8]
    dff10 = df10[df10.RouteType==value9]
    dff11 = df11[df11.RouteType==value10]
    dff12 = df12[df12.PointName==value11]
    dff13 = df13[df13.TourismType==value12]
    dff14 = df14[df14.TransportNodeName==value13]
    dff15 = df15[df15.TransportNodeName==value14]
    dff16 = df16[df16.Year==value15]
    fig = px.histogram(dff, x='DaysMax', y='TouristsCount')
    fig2 = px.histogram(dff2, x='TouristsCount', y='AvPointPrice')
    fig3= px.histogram(dff3, x='PointTime', y='OrderDay')
    fig4 = px.histogram(dff4, x='Tourists', y='AvPrice')
    fig5 = px.histogram(dff5, x='Tourists', y='PlanCost')
    fig6 = px.histogram(dff6, x='PartOfCommon', y='TripDays')
    fig7 = px.histogram(dff7, x='FirstNum', y='FirstPlace')
    fig8= px.histogram(dff8, x='Tourist', y='AvCost')
    fig9 = px.histogram(dff9, x='TourDay', y='TouristsCount')
    fig10 = px.histogram(dff10, x='AvDaysClosed', y='TransportsThread')
    fig11 = px.histogram(dff11, x='AvDaysClosed', y='TransportThread')
    fig12 = px.histogram(dff12, x='MaxDays', y='MinDays')
    fig13= px.histogram(dff13, x='AvDaysTrip', y='AvCostTrip')
    fig14 = px.histogram(dff14, x='TouristsThread', y='TransportThread')
    fig15 = px.histogram(dff15, x='TouristsThread', y='TransportThread')
    fig16 = px.histogram(dff16, x='Year', y='December')
    return fig,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10,fig11,fig12,fig13,fig14,fig15,fig16


if __name__ == '__main__':
    app.run(debug=True)
