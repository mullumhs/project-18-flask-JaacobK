from flask import Flask, request, redirect

app = Flask(__name__)

todos= ["adwawd", "hamadswui"]

#todo list
@app.route('/')

def list_todos():

    s = ""
    for i in todos:
        s += f"{i} <br>"
    return s

@app.route('/add/<task>')

def add_todo(task):
    todos.append(task)

#hi 
@app.route('/hi/<name>')

def hi(name):

    return f'hi {name}'

#bye
@app.route('/bye/<name>')

def bye(name):

    return f'bye {name}'

#repeat words
@app.route('/repeat/<word>/<int:amount>')

def reapeating(word, amount):
    s = ""
    for i in range(amount):
        s += f"{word} <br>" 
    return s

#clac
@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')

def calculator(num1, operation, num2):
    if operation == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    elif operation == "-":
        return f"{num1} - {num2} = {num1 - num2}"
    elif operation == "*":
        return f"{num1} * {num2} = {num1 * num2}"
    elif operation == "÷":
        return f"{num1} ÷ {num2} = {num1 / num2}"

#query
@app.route('/search')

def search():
    query = request.args.get("q", "")
    category = request.args.get('category', 'all')
    return f"searching for {query} in the category {category}"

if __name__ == '__main__':



    app.run(debug=True)