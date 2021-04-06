import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import chart_studio.tools as tls

from astar import *

chart_studio.tools.set_credentials_file(username='TucilStimaIP4', api_key='mHblEi7fouhLhed0Fk12')

def getIndexFromName(graph, name):
    for i in range(len(graph)):
        if graph[i].name[0] == name:
            return i

def createMap(graph, src, dest):
    lintang =[]
    bujur =[]
    fig = go.Figure(go.Scattermapbox(
        mode = "markers+lines",
        lon = [],
        lat = [],
        marker = {'size': 10}))
    astaresult = astar(graph[getIndexFromName(graph,src)],graph[getIndexFromName(graph,dest)],graph)
    astaresult2 = astar(graph[getIndexFromName(graph,dest)],graph[getIndexFromName(graph,src)],graph)

    result = astaresult[0]
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
                    line_color = '#FF0000'))
            else:
                fig.add_trace(go.Scattermapbox(
                    mode = "lines",
                    lon = [i.name[2],x[2]],
                    lat = [i.name[1],x[1]],
                    showlegend = False,
                    hoverinfo = "none",
                    line_color = '#000000'))
    for i in graph:
        if (len(result) != 0 and (i.name[0]== result[0] or i.name[0] == result[-1])):
            fig.add_trace(go.Scattermapbox(
                mode = "markers",
                lon = [i.name[2]],
                lat = [i.name[1]],
                name = i.name[0],
                hoverinfo = 'name',
                marker_color = '#9E2B2B',
                marker = {'size':20}))
        elif(i.name[0] in result):
            fig.add_trace(go.Scattermapbox(
                mode = "markers",
                lon = [i.name[2]],
                lat = [i.name[1]],
                name = i.name[0],
                hoverinfo = 'name',
                marker_color = '#cbd967',
                marker = {'size':20}))
        else:
            fig.add_trace(go.Scattermapbox(
                mode = "markers",
                lon = [i.name[2]],
                lat = [i.name[1]],
                name = i.name[0],
                hoverinfo = 'name',
                marker_color = '#000000',
                marker = {'size':20}))

    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': float(graph[0].name[2]), 'lat': float(graph[0].name[1])},
            'style': "light",
            'center': {'lon': float(graph[0].name[2]), 'lat': float(graph[0].name[1])},
            'zoom': 15})

    plot_url = py.plot(fig,auto_open=False)
    if (astaresult[1]>astaresult2[1]):
        output = [plot_url, astaresult2[1]]
    else:
        output = [plot_url, astaresult[1]]
    return(output)