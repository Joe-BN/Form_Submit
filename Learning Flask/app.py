from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('learnt.html')

@app.route('/', methods = ['POST', 'GET'])
def getvalue():
    password = request.form['pwd']
    email = request.form['email']

    return render_template('pass.html', email=email, pwd=password,)


if __name__ == '__main__':
    app.run(debug=True)
