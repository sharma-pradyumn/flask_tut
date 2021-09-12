from flask import Flask, url_for , render_template, redirect
from form import Contactform

app=Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def contact():
    #creating object of the class
    form =Contactform()
    #method 1
    # if form.validate_on_submit():
    #     return redirect(url_for('success'))
    # return render_template('index.html', form=form)

    #method 2
    # if request.method == 'POST' and form.validate():
    #     user = User(form.username.data, form.email.data,
    #                 form.password.data)
    #     db_session.add(user)
    #     flash('Thanks for registering')
    #     return redirect(url_for('login'))
    # return render_template('register.html', form=form)
    
    
