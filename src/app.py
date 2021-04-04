from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import plotly.graph_objects as go
from astar import *
app = Flask(__name__)

def createMap(graph):
    lintang =[]
    bujur =[]
    fig = go.Figure(go.Scattermapbox(
        mode = "markers+lines",
        lon = [],
        lat = [],
        marker = {'size': 10}))
    result = astar(graph[1],graph[19],graph)
    print(result)
    for i in graph:
        lintang.append(i.name[2])
        bujur.append(i.name[1])
        for x,y in i.adjacentNodes.items():
            if (i.name[0] in result and x[0] in result):
                fig.add_trace(go.Scattermapbox(
                    mode = "lines",
                    lon = [i.name[2],x[2]],
                    lat = [i.name[1],x[1]],
                    showlegend = False,
                    hoverinfo = "none",
                    line_color = '#FFFFFF'))
            else:
                fig.add_trace(go.Scattermapbox(
                    mode = "lines",
                    lon = [i.name[2],x[2]],
                    lat = [i.name[1],x[1]],
                    showlegend = False,
                    hoverinfo = "none",
                    line_color = '#000000'))
    for i in graph:
        fig.add_trace(go.Scattermapbox(
            mode = "markers",
            lon = [i.name[2]],
            lat = [i.name[1]],
            name = i.name[0],
            hoverinfo = 'name',
            marker_color = '#000000',
            marker = {'size':20}))

    # fig.update_traces(marker_color = "#00000")

    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': 10, 'lat': 10},
            'style': "open-street-map",
            'center': {'lon': -20, 'lat': -20},
            'zoom': 1})

    fig.write_html("templates/check.html")

@app.route('/', methods=['GET'])
def dropdown():
    result = makeGraph(parse("test.txt"))
    nodeA = [i.name[0] for i in result]
    nodeB = [i.name[0] for i in result]
    return render_template('main.html', nodeA=nodeA, nodeB=nodeB)
    
@app.route('/')
def route():
    createMap(makeGraph(parse('test.txt')))
    return render_template('check.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2211)

