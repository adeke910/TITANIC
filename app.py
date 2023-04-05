# import Flask and create an instance of the Flask object
import flask
import pickle
import pandas as pd

# Use pickle to load in the trained model
# with open(f'model/titanic_model_stkd.pkl', 'rb') as f:
# # model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates',
                  static_folder='static')


@app.route('/')
def home():
    return flask.render_template('main.html')


@app.route("/submit", methods=['GET', 'POST'])
def form_submit():
    age = flask.request.form['age']
    sex = flask.request.form['sex']
    Family = flask.request.form['Family']
    Pclass = flask.request.form['Pclass']
    Embarked = flask.request.form['Embarked']
    return flask.render_template('main.html')


if __name__ == '__main__':
    app.run()
