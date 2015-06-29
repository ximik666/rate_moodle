# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
import sys, codecs,
reload(sys)
sys.setdefaultencoding('utf-8')
import sqlite3 as sql
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

def select_account_holder(params=()):
    con = sql.connect("rate.db")
    cur = con.cursor()
    if params == ():
        cur.execute("select * from fio")
    else:
        string = "select"
        for i in xrange(len(params) - 1):
            string += "%s,"
        string += "%s"
        string += " from account_holder"

        result = cur.execute(string)
        con.close()
        return result.fetchall()

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/rate/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("5000")
  )