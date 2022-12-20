import json
import mysql.connector
from flask import Blueprint,Flask,request,make_response,render_template
from datetime import datetime,timedelta,date,time
import pandas as pd

app = Flask(__name__,template_folder='./templates')


df = pd.read_csv(r"D:\\Main Data Folder\\Downloads\\amazon_com-product_reviews__20200101_20200331_sample.csv",)
gg = df[["Review Content","Brand"]]


def xyz(a):
    if request.method == 'POST':
        search = a['product name']
        ff = gg.where(gg["Brand"]==search)
        ff.dropna(inplace=True)
        return render_template('result.html',result=ff)
    else:
        return render_template('input.html')

@app.route("/", methods=['GET','POST'])
def abc():
    return xyz(request.form)

app.run(host='0.0.0.0', port='8080',debug=True)