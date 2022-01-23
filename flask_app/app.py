from flask import Flask, render_template, flash, redirect, request, url_for
import pandas as pd
import pickle

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "password"

df = pd.read_csv("model\\fraud_data_final.csv")

with open('model\\fraud_model_final.bin', 'rb') as f_in:
    model = pickle.load(f_in)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if request.form["transaction_id"] == "":
            flash(" Please enter a name ", "info")
            return render_template("home.html")
        
        id = request.form["transaction_id"]
        
        try:
            if id[0].lower() != 'c':
                raise ValueError
            row = df.loc[df['nameOrig']==int(id[1:])]
        except ValueError:
            return render_template("home.html", error="Enter valid Transaction ID")
        if row.shape[0] == 0:
            return render_template("home.html", prediction=0)
        
        else:
            feature_list = list(row.iloc[0,[1,2,3,4,5,6,7]])
            name_list = list(row.iloc[:,[1,2,3,4,5,6,7]])
            prediction = model.predict([feature_list])
            print(feature_list)
            print( prediction)
            return render_template("home.html", row=zip(name_list, feature_list), prediction=prediction[0])
    else:
        return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()