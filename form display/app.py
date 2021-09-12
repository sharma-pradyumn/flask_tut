from flask import *
app = Flask(__name__) 
@app.route('/')
def customer():
    return render_template("customer.html")
@app.route('/success',methods=['POST','GET'])
# This tells Flask that this view function accepts GET and POST requests, 
#overriding the default, which is to accept only GET requests. 
#The HTTP protocol states that GET requests are those that return information to the client (the web browser in this case). 
#All the requests in the application so far are of this type. POST requests are typically used when the browser submits form data to the server
def print_data():
    if request.method=='POST':
        result=request.form
        return render_template("result_data.html",result=result)
if __name__=="__main__":
    app.run(debug=True)
