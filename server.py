from flask import Flask, render_template, request, redirect, url_for
import convert as cc

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("sample.html")

@app.route('/save',methods=["POST","GET"])
def save():
    if request.method == "POST" :
        f = open('input.txt','w')
        f.write(request.form['code'])
        f.close()
        return render_template('sample.html',content1 = request.form['code'])
    else:
        return redirect(url_for('home'))

@app.route('/convert', methods=['POST','GET'])
def convert():
    if request.method == "POST":
        cc.changecode()
        f = open('input.txt','r')
        s = f.read()
        f.close()
        f1 = open('output.txt','r')
        s1 = f1.read()
        f1.close()
        return render_template('sample.html',content1 = s,content2 = s1)
    else:
        return redirect(url_for('home'))

@app.route('/refresh',methods=['POST','GET'])
def refresh():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
