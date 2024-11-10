from flask import Flask, render_template, url_for

app = Flask(__name__)


#base
@app.route('/')

def basic():

    return render_template('base.html')

#greet
@app.route('/greet/<name>')

def greet(name):

    return render_template('greet.html', name=name)

#inventory
@app.route('/inventory')
def inventory():
    inventory_items = ["apple", "dingleberry", "banana", "dragonfruit"]
    return render_template('inventory.html', inventory=inventory_items)

#Inheritance
@app.route('/test/<message>')

def test(message):

    return render_template('test.html', message=message)

#url_for and Static Assets
@app.route('/profile/<username>')

def profile(username):

    return render_template('profile.html', username=username)



if __name__ == '__main__':

    app.run(debug=True)