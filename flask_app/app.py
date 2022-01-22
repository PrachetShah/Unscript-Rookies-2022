from flask import Flask, render_template, flash, redirect, request, url_for
from datetime import timedelta
from markupsafe import escape
import pandas as pd
import pickle

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "password"

df1 = pd.read_csv("model\\fraud_data1_1_1.csv")
df2 = pd.read_csv("model\\fraud_data1_1_2.csv")
df3 = pd.read_csv("model\\fraud_data2.csv")

df = pd.concat([df1,df2,df3])

with open('model\\fraud_model.bin', 'rb') as f_in:
    model = pickle.load(f_in)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if request.form["transaction_id"] == "":
            flash(" Please enter a name ", "info")
            return render_template("home.html")
        
        id = request.form["transaction_id"]
        
        row = df.loc[df['nameOrig']==int(id[1:])]
        
        prediction = model.predict([list(row.iloc[0,[1,2,3,4,5,7,8]])])
        print( prediction )
        return render_template("home.html", row=list(row.values.tolist()), prediction=prediction)
    else:
        return render_template("home.html")
    
@app.route('/about')
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug = True)