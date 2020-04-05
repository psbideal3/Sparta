from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template("HW_4.html")

@app.route('/mypage')
def mypage():
   return 'This is My Page!'

if __name__ == '__main__':
   app.run('0.0.0.0',port=4500,debug=True)