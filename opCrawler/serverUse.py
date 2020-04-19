from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def mainPage():
   return render_template('mainPage.html!')

@app.route('/mypage')
def mypage():
   return 'This is My Page!'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)


