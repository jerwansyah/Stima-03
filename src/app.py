from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import plotly.graph_objects as go
app = Flask(__name__)

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

@app.route('/')
def route():
    createMap()
    return render_template('check.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2211)

