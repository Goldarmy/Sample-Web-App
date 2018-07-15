from flask import render_template, request
from Sample_Web_App import app
from Sample_Web_App.models import VEHICLETBL


@app.route('/')
def index():
    return 'Hello Second World'


@app.route('/vehicles')
def vehicles():
    vehicles = VEHICLETBL.query.all()
    return render_template('vehicles.html', vehicles=vehicles)
    #mssql://vlogin@project2server:0Vpassword@project2server.database.windows.net:1433/SoapDatabase?driver="ODBC Driver 13 for SQL Server" 
    #connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:project2server.database.windows.net,1433;Database=SoapDatabase;Uid=vlogin@project2server;Pwd=0Vpassword;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
  
    #cursor = connection.cursor()  
    #cursor.execute("SELECT * FROM VEHICLE_TBL")
    #for row in cursor:
    #    print(row[0], '---', row[1])
    #return render_template('vehicles_c.html', vehicles=cursor)


@app.route('/shopping')
def shopping():
    shopping_list = ['Bread', 'Eggs', 'Flour', 'Milk']
    return render_template('shopping.html', shopping_list=shopping_list)


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h1>Post Id is %s<h1>" % post_id

