from flask import *
app=Flask(__name__)
app.secret_key="abcd"

@app.route('/')
def start():
    return redirect('/welcome')
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/profile')
def view_profile():
    if "email" in session:
        email=session["email"]
        return "Hello "+email
    else:
        return "Please login first"

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/success',methods=['POST','GET'])
def success():
    email=request.form['email']
    password=request.form['password']
    if email=="pradyumn@gmail.com":
        if password=="1234":
            res=make_response(render_template("success.html"))
            session["email"]=email
            return res
    else:
        return render_template("login.html")

@app.route('/logout')  
def logout():  
    if "email" in session:  
        session.pop("email",None)  
        return render_template('logout.html');  
    else:  
        return '<p>user already logged out</p>'  

if __name__ == '__main__':  
    app.run(debug = True)  
