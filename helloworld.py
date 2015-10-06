#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
from flask import Markup
from flask import Response

import subprocess
import hashlib
import os
import time

app = Flask(__name__)

def sha256sum( s ):
    foo = hashlib.sha256()
    foo.update( bytes( s, "utf-8" ))
    return foo.hexdigest()

def remote_run_file( filename ):
    val =  filename + "\n"

    try:
        val += subprocess.check_output([ "./runscm.sh", filename, filename ]).decode( "utf8" )

    except subprocess.CalledProcessError as e:
        val += e.output.decode( "utf8" )
        val += "\nError: program reached resource limits, sorry.\n"

    return val

def has_code_file( filename ):
    filepath = "codefiles/" + filename.replace("/", "")

    if os.path.exists( filepath ):
        return filepath
    else:
        return False

def run_code( code ):
    if len( code ) < (1024 * 40):
        filename = sha256sum( code )[0:8] + ".scm"
        filepath = "codefiles/" + filename

        if not os.path.exists( filepath ):
            print( "Writing to " + filename + "..." )
            f = open( filepath, "w" )
            f.write( code )
            f.close( )

        return remote_run_file( filename )

    else:
        return "Code is too large!"

def run_file( filename ):
    #filepath = "codefiles/" + filename.replace("/", "")
    filepath = has_code_file( filename )

    if filepath:
        return remote_run_file( filename )
    else:
        return "File does not exist.\n"

def print_file( filename ):
    filepath = has_code_file( filename )

    if filepath:
        f = open( filepath, "r" )
        val = f.read( )
        f.close()
        return val
    else:
        return "File does not exist.\n"

@app.route('/netlisp/')
def hello_world():
    return """<html>
    <head />
    <body>
        <a href='/netlisp/hello/'>foo bar</a>
        <br />
        <a href='/netlisp/login'>login thing</a>
        <br />
        <a href='/netlisp/coderun'>run code</a>
        <br />
        <a href='/netlisp/code'>list code</a>
        <br />
        <a href='/netlisp/codebrowse'>scriptless code browser</a>
    </body>
    <html>"""

@app.route('/netlisp/hello/')
@app.route('/netlisp/hello/<name>')
def foobar(name=None):
    return render_template( "./asdf.html", name=name )

@app.route('/netlisp/coderun/', methods=["POST", "GET"])
@app.route('/netlisp/coderun',  methods=["POST", "GET"])
@app.route('/netlisp/coderun/<filename>')
def meh(filename=None):
    code = None

    if request.method == "POST":
        code = request.form["code"]
    elif request.method == "GET" and "code" in request.args:
        code = request.args.get("code", "")

    if filename:
        return Response( run_file( filename ),
                mimetype="text/plain" )
        #resp = Response( run_file( filename ),
        #         mimetype="text/plain" )
        #resp.headers["Access-Control-Allow-Origin"] = "*"
        #return resp

    elif code:
        return Response( run_code( code ),
                mimetype="text/plain" )
        #resp = Response( run_code( code ),
        #         mimetype="text/plain" )
        #resp.headers["Access-Control-Allow-Origin"] = "*"
        #return resp

    return render_template( "codething.html", output=None )

@app.route("/netlisp/code")
@app.route("/netlisp/code/<filename>")
def thing_print_file(filename=None):
    if filename:
        return Response( print_file( filename ), mimetype="text/plain" )
    else:
        accum = ""
        for thing in os.listdir( "codefiles" ):
            accum += thing + "\n"

        #resp = Response( accum, mimetype="text/plain" )
        #resp.headers["Access-Control-Allow-Origin"] = "*"
        #return resp
        return Response( accum, mimetype="text/plain" )

@app.route("/netlisp/code-io/<filename>")
def print_io(filename=None):
    if has_code_file( filename ):
        foo = print_file( filename )
        bar = run_file( filename )
        val = foo + "\n\n" + "="*80 + "\n\n" + bar
        return Response( val, mimetype="text/plain" )
    else:
        return Response( "File does not exist.", mimetype="text/plain" )

@app.route("/netlisp/codebrowse")
def html_code_browser():
    accum = """<!doctype html>
    <html>
    <head><title>Code list</title></head>
    <body>
        """

    for thing in os.listdir( "codefiles" ):
        created = time.ctime( os.path.getctime( "codefiles/" + thing ))

        accum += '<strong>' + thing + '</strong>'
        accum += ', created on ' + created + ' '
        accum += ' || '
        accum += '<a href="/netlisp/code/'      + thing + '">View source</a>'
        accum += ' || '
        accum += '<a href="/netlisp/coderun/' + thing + '">Run code</a>'
        accum += '<br />'

    accum += "</body></html>"

    return accum
    

@app.route('/netlisp/login', methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        return render_template( "login.html",
                username=request.form["username"],
                password=request.form["password"] )

    return render_template( "login.html", username=None, password=None )

if __name__ == '__main__':
    app.run(debug=True)
    app.run()
    #app.debug=False
    #app.run( host="0.0.0.0", debug=False )
