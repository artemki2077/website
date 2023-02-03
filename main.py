from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Artemkrut'}  # выдуманный пользователь
    return render_template("index.html",
                           title='Home',
                           user=user,
                           range=range)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
