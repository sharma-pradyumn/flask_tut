# In flask,the cookies are associated with the Request object as the dictionary object of all the cookie variables and their values transmitted by the client.
# In Flask, the cookies are set on the response object by using the set_cookie() method on the response object
# The response object can be formed by using the make_response() method in the view function.
from flask import *
app=Flask(__name__)

@app.route('/error')
def error():
    return "<p><strong>Please enter correct password</strong></p>"

@app.route('/')  
def login():  
    return render_template("login.html")  

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        if password=="hello":
            resp=make_response(render_template("success.html"))
            resp.set_cookie('email',email)
            return resp
#Here cookies are used to send data from one page to another to a third page
        else:
            return redirect(url_for('error'))

@app.route('/viewprofile')  
def profile():  
    email = request.cookies.get('email')  
    resp = make_response(render_template('profile.html',name = email))  
    return resp  
  
if __name__ == "__main__":  
    app.run(debug = True)  
