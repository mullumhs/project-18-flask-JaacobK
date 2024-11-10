from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)



@app.route('/contact', methods=['GET', 'POST'])

def contact():

    if request.method == 'POST':

        name = request.form['name']

        email = request.form['email']

        message = request.form['message']

        # Here you would typically save this data or send an email

        return redirect(url_for('thankyou', name=name, message=message))

    return render_template('contact.html')



@app.route('/thankyou')

def thankyou():

    name = request.args.get('name')

    message = request.args.get('message')

    return render_template('thankyou.html', name=name, message=message)



if __name__ == '__main__':

    app.run(debug=True)