# Import libraries 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Internal imports from application
from app import app, server
from pages import index, predictions, insights, process
from joblib import load


# Sections of homepage

# Navigation bar
navbar = dbc.NavbarSimple(
    brand='Airbnb Price Predictor',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
        dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')), 
    ],
    sticky='top',
    color='light', 
    light=True, 
    dark=False
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('James Yeh', className='mr-2'),
                                html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/James-yeh'), 
                            ], 
                            className='lead'
                        )
                    ]
                ),
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('Allen Dela Virgen', className='mr-2'),
                                html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/matthewblackbu/Airbnb/commits?author=Abdelapv53'), 
                            ], 
                            className='lead'
                        )
                    ]
                ),
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('Matthew Blackburn', className='mr-2'),
                                html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/matthewblackbu'), 
                            ], 
                            className='lead'
                        )
                    ]
                ),
            ]
        )
    ]
)

# App layout (TODO: Clean)
# Add more pages (About page/results page)
# Working layout
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        navbar,
        dbc.Container(id='page-content', className='mt-4'),
        html.Hr(),
        footer
    ],
    # style={
    #     'background-image':'url("/assets/background.jpg")'
    # }
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/insights':
        return insights.layout
    elif pathname == '/process':
        return process.layout
    else:
        return dcc.Markdown('## Page not found')

if __name__ == '__main__':
    app.run_server(debug=True)
