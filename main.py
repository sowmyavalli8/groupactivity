# creating a flask application that will fetch data from the database and display it on the web page

from flask import Flask, render_template, request, redirect, url_for
from database import Database

def createApp():
    # creating a flask application
    app = Flask(__name__)

    # creating a database object
    user = "root"
    password = "root"
    host = "localhost"
    database = "c361"
    table_name = "test"
    mydb = Database(user,password,host,database,table_name)

    # this function will simply fetch data from db and display it on homepage
    @app.route('/')
    def index():
        myresult = mydb.fetchAllData(table_name)
        return render_template("index.html", data=myresult)
    

    # creating a route to insert data into the database using a form
    @app.route('/insert', methods=['GET','POST'])
    def insert():
        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']
            mydb.insertData(table_name,name,age)
            return redirect(url_for('index'))
        return render_template("insert.html")
    
    # creating a route to search data from the database using a form
    @app.route('/search',methods=['GET','POST'])
    def search():
        if request.method == 'POST':
            name = request.form['name']
            result = mydb.searchData(table_name,name)
            return render_template("search.html",data=result)
        return render_template("search.html")

    return app

if __name__ == "__main__":
    app = createApp()
    app.run()