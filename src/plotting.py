import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import chart_studio.tools as tls

from astar import *

chart_studio.tools.set_credentials_file(username='Zenovore', api_key='WVo1aIq79gDxkydrcXbn')

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
    result = astar(getIndexFromName(graph,src),getIndexFromName(graph,dest),graph)
    # print(result)
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
            'center': {'lon': graph[0].name[2], 'lat': graph[0].name[1]},
            'style': "open-street-map",
            'center': {'lon': -20, 'lat': -20},
            'zoom': 1})

    plot_url = py.plot(fig,auto_open=False)
    return(plot_url)

# result = createMap(makeGraph(parse("test.txt")))
# print(result)