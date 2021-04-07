import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import chart_studio.tools as tls

from astar import *

chart_studio.tools.set_credentials_file(username='TucilStimaIP4', api_key='mHblEi7fouhLhed0Fk12')

def getIndexFromName(graph, name): # Mencari Index berdasarkan nama pada Graph
    for i in range(len(graph)):
        if graph[i].name[0] == name:
            return i

def createMap(graph, src, dest): # Membuat Mapbox, dengan bantuan Plotly
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
    for i in graph: # Melakukan Iterasi untuk setiap node pada graph
        lintang.append(i.name[2]) # Memasukkan nilai lintang pada sebuah list
        bujur.append(i.name[1]) # Memasukkan nilai buju pada sebuah list
        for x,y in i.adjacentNodes.items(): # Melakukkan iterasi untuk setiap Node yang dapat diakses
            if (i.name[0] in result and x[0] in result): # Membuat garis berwarna merah untuk result 
                fig.add_trace(go.Scattermapbox( # Membuat Garis pada mapbox, berwarna merah untuk result
                    mode = "lines",
                    lon = [i.name[2],x[2]],
                    lat = [i.name[1],x[1]],
                    showlegend = False,
                    hoverinfo = "none",
                    line_color = '#FF0000'))
            else:
                fig.add_trace(go.Scattermapbox( # Membuat Garis pada mapbox, berwarna hitam untuk garis lainnya
                    mode = "lines",
                    lon = [i.name[2],x[2]],
                    lat = [i.name[1],x[1]],
                    showlegend = False,
                    hoverinfo = "none",
                    line_color = '#000000'))
    for i in graph:
        if (len(result) != 0 and (i.name[0]== result[0] or i.name[0] == result[-1])):
            fig.add_trace(go.Scattermapbox( # Membuat Marker pada mapbox, berwarna Merah untuk Marker Node Awal dan Node Tujuan
                mode = "markers",
                lon = [i.name[2]],
                lat = [i.name[1]],
                name = i.name[0],
                hoverinfo = 'name',
                marker_color = '#9E2B2B',
                marker = {'size':20}))
        elif(i.name[0] in result):
            fig.add_trace(go.Scattermapbox( # Membuat Marker pada mapbox, berwarna Hijau untuk Marker yang dilewati Node Awal dan Tujuan
                mode = "markers",
                lon = [i.name[2]],
                lat = [i.name[1]],
                name = i.name[0],
                hoverinfo = 'name',
                marker_color = '#cbd967',
                marker = {'size':20}))
        else:
            fig.add_trace(go.Scattermapbox( # Membuat Marker pada Mapbox, berwarna Hitam untuk marker lainnya
                mode = "markers",
                lon = [i.name[2]],
                lat = [i.name[1]],
                name = i.name[0],
                hoverinfo = 'name',
                marker_color = '#000000',
                marker = {'size':20}))

    fig.update_layout( # Membuat layout untuk mengatur zoom dan lokasi awal mapbox
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': float(graph[0].name[2]), 'lat': float(graph[0].name[1])},
            'style': "light",
            'center': {'lon': float(graph[0].name[2]), 'lat': float(graph[0].name[1])},
            'zoom': 15})

    plot_url = py.plot(fig,auto_open=False) # Melakukan plotting, dan mengembalikan link untuk ditangkap dan dilakukan Embed pada main.html
    if (astaresult[1]>astaresult2[1]):
        output = [plot_url, astaresult2[1]]
    else:
        output = [plot_url, astaresult[1]]
    return(output) # Mengembalikan nilai dalam bentuk List