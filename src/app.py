from flask import Flask, render_template, url_for, request, redirect, flash
from flask import g as gobj
from flask_bootstrap import Bootstrap
import plotly.graph_objects as go
from werkzeug.utils import secure_filename
import os
from astar import *
from plotting import *

UPLOAD_FOLDER = '../test/'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
test = app.app_context()
test.push()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)

gobj.result = None
gobj.nodeA = []
gobj.nodeB = []
gobj.src = ''
gobj.dest = ''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def route()
    with test:
        result = gobj.result
        nodeA = gobj.nodeA
        nodeB = gobj.nodeB
        src = gobj.src
        dest = gobj.dest
    return render_template('main.html', nodeA=nodeA, nodeB=nodeB, src='src', dest='dest', pranala='')

@app.route('/upload', methods=['POST', 'GET'])
def uploadFile():
    if request.method == 'POST':
        if 'sabmeet' in request.form:
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return render_template('main.html')
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
                with test:
                    gobj.result = result
                    gobj.nodeA = nodeA
                    gobj.nodeB = nodeB
                    gobj.src = nodeA[0]
                    gobj.dest = nodeB[0]
                    # print(gobj.result)
                    # print(gobj.nodeA)
                    # print(gobj.nodeB)
                    # print(gobj.src)
                    # print(gobj.dest)
            return render_template('main.html', nodeA=nodeA, nodeB=nodeB, src=src, dest=dest, pranala='')
    if request.method == 'GET':
        if 'getMap' in request.form:
            with test:
                gobj.src = request.args.get('src')
                gobj.dest = request.args.get('dest')
                pranala = createMap(src, dest, gobj.result)
            return render_template('main.html', nodeA=nodeA, nodeB=nodeB, src=src, dest=dest, pranala=pranala)
    # return render_template('main.htmlplotting return render_template('main.html')

# @app.route('/upload', methods=['POST', 'GET'])
# @app.route('/astar', methods=['POST', 'GET'])
# def viewMap():
#     if request.method == 'POST':
#         if 'getMap' in request.form:
#             with test:
#                 gobj.src = request.form.get('src')
#                 gobj.dest = request.form.get('dest')
#                 # createMap(src, dest, gobj.result)
#    return render_template('main.html', nodeA=gobj.nodeA, nodeB=gobj.nodeB, src=gobj.src, dest=gobj.dest)
#    return render_template('main.html', nodeA=nodeA, nodeB=nodeB, src=src, dest=dest)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2211)

