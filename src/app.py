from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import plotly.graph_objects as go
from astar import *

app = Flask(__name__)
Bootstrap(app)

def createMap():
    fig = go.Figure(go.Scattermapbox(
        mode = "markers+lines",
    lon = [10, 20, 30,10],
    lat = [10, 20,30,10],
        marker = {'size': 10}))

    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': 10, 'lat': 10},
            'style': "stamen-terrain",
            'center': {'lon': -20, 'lat': -20},
            'zoom': 1})

    fig.write_html("templates/check.html")

# @app.route('/', methods=['POST, GET'])
# def browse():
#     filename = 'yee'
#     return render_template('main.html', filename=filename)

@app.route('/', methods=['GET'])
def dropdown():
    result = makeGraph(parse("test.txt"))
    nodeA = [i.name[0] for i in result]
    nodeB = [i.name[0] for i in result]
    return render_template('main.html', nodeA=nodeA, nodeB=nodeB)

@app.route('/')
def route():
    createMap()
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2211)

