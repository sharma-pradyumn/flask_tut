from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message


app=Flask(__name__)
mail=Mail(app)
#app.config defines the various values of properties of the app object. Eg debug=True
#Here, DATABASE_URI gives us the location of the database we are creating
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///students.sqlite3"
app.config['SECRET_KEY'] = "random string"
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'iscariotpriest2@gmail.com'
app.config['MAIL_PASSWORD'] = 'crimson_fucker'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
#The DB object contains helper functions for ORM operations.
# It also provides a parent Model class using which user defined models are declared
db=SQLAlchemy(app)

class students(db.Model):
   id = db.Column('studentid', db.Integer, primary_key = True)
   name = db.Column('name',db.String(100))
   city = db.Column('city',db.String(50))
   email= db.Column('email',db.String(100))
   def __init__(self,name, city,email):
        self.name = name
        self.city = city
        self.email =email

#The User class created above inherits from db.Model, a base class for all models from Flask-SQLAlchemy.
# This class defines several fields as class variables. Fields are created as instances of the db.Column class, which takes the field type as an argument,
# plus other optional arguments that, for example, allow me to indicate which fields are unique and indexed, which is important so that database searches are efficient.
    

# The following session methods perform CRUD operations −
# db.session.add(model object) − inserts a record into mapped table
# db.session.delete(model object) − deletes record from table
# model.query.all() − retrieves all records from table (corresponding to SELECT query).

@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all())

@app.route('/new',methods=['GET','POST'])
def new():
    if request.method=='GET':
        return render_template('new.html')
    else:
        try:
            student=students(request.form['name'],request.form['city'],request.form['email'])
            db.session.add(student)
            db.session.commit()
            flash('Successfully added')
            
        except:
            db.session.rollback()
            flash('Cannot Add')
        finally:
            return redirect(url_for('show_all'))


@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='GET':
        return render_template('delete.html')
    else:
        try:
            id=request.form['studentid']
            students.query.filter_by(id=int(id)).delete()
            db.session.commit()
            flash('Deleted')
        except:
            flash('Cannot Delete with '+id)
        finally:
            return redirect(url_for('show_all'))

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='GET':
        return render_template('delete.html')
    else:
        name=request.form['studentname']
        results=students.query.filter_by(name=name)
        return render_template('show_all.html', students = results)

@app.route('/email',methods=['GET','POST'])
def email():
    if request.method=='GET':
        return render_template('email.html')
    else:
        id=request.form['studentid']
        target=students.query.filter_by(id=int(id)).value('email')
        try:
            msg = Message('Hello', sender = 'iscariotpriest2@gmail.com', recipients = [target])
            msg.body = "Hello Flask message sent from Flask-Mail"
            mail.send(msg)
            flash("Mail sent to "+target)
        except:
            flash('Cannot Send mail to '+target)
        finally:
            return redirect(url_for('show_all'))

        


if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
    