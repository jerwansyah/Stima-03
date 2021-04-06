from flask import Flask, render_template, url_for, request, redirect, flash
from flask_bootstrap import Bootstrap
import plotly.graph_objects as go
from werkzeug.utils import secure_filename
import os
from astar import *

UPLOAD_FOLDER = '../test/'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)

result = None
filename = str()
nodeA = []
nodeB = []
src = ''
dest = ''

def dibaging(string):
    print('********** ' + string + ' **********')
    print(nodeA)
    print(nodeB)
    print(namafile)
    print(A)
    print(B)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def getIndexFromName(graph, name):
    for i in range(len(graph)):
        if graph[i].name[0] == name:
            return i


# @app.route('/', methods=['GET'])
# def dropdown():
#     result = makeGraph(parse(file.filename))
#     nodeA = [i.name[0] for i in result]
#     nodeB = [i.name[0] for i in result]
#     return render_template('main.html', nodeA=nodeA, nodeB=nodeB)

@app.route('/')
def route(filename=None, nodeA=nodeA, nodeB=nodeA, src=src, dest=dest, result=result):
    return render_template('main.html', filename=filename, nodeA=nodeA, nodeB=nodeB, src=src, dest=dest, result=result)

@app.route('/upload', methods=['POST', 'GET'])
def uploadFile():
    global filename, nodeA, nodeB, src, dest, result
    # global namafile, nodeA, nodeB, result, src, dest
    if request.method == 'POST':
        if 'sabmeet' in request.form:
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return render_template('main.html', filename='No file uploaded', nodeA=nodeA, nodeB=nodeB, src=src, dest=dest, result=result)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect('main.html')
            if file and allowed_file(file.filename):
                # submit 2x => RTE
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                with open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as f:
                    result = makeGraph(parse(f))
            
                nodeA = [i.name[0] for i in result]
                nodeB = [i.name[0] for i in result]
                src = nodeA[0]
                dest = nodeB[0]
    return render_template('main.html', filename=filename, nodeA=nodeA, nodeB=nodeB, src=src, dest=dest, result=result)
    # return redirect(url_for('route', filename=namafile, nodeA=nodeA, nodeB=nodeB, src=A, dest=B, **request.args))

@app.route('/astar', methods=['POST', 'GET'])
def viewMap():
    global filename, nodeA, nodeB, src, dest, result
    if request.method == 'POST':
        if 'getMap' in request.form:
            src = request.form.get('nA')
            dest = request.form.get('nB')
            # createMap(src, dest, result)
    return render_template('main.html', filename=filename, nodeA=nodeA, nodeB=nodeB, src=src, dest=dest, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2211)