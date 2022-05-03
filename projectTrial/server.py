from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        userEmail = request.form['email']
        password = request.form['password']
        if(userEmail == 'michael@gamil.com' and password == '1234'):
            return render_template('index.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

if __name__ == '__main__':
   app.run()
