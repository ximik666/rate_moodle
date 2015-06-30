# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
import sys, codecs
reload(sys)
sys.setdefaultencoding('utf-8')
import sqlite3 as sql
from flask import Flask, json, render_template, request, url_for,jsonify

# Initialize the Flask application
app = Flask(__name__)

def select_account_holder():
    con = sql.connect("rate.db")
    cur = con.cursor()
    result = cur.execute("select * from rate")
    print result.fetchall()

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

@app.route('/star')
def stars():
    return render_template('stars.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/rate/', methods=['POST'])
def rate():
    id_course=request.form['id_course']
    id_user=request.form['id_user']
    select_account_holder()
    return render_template('form_action.html', id_course=id_course, id_user=id_user)

@app.route('/post', methods = ['PUT','POST'])
def post():
    # Get the parsed contents of the form data
    print request.get_json(force=True)
    return jsonify(request.get_json(force=True))

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("5001")
  )