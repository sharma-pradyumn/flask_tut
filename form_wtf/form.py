from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField 
from wtforms.validators import DataRequired , Length, Email
from flask_wtf.recaptcha.fields import RecaptchaField

#To use the wtf_form , We need to create a class of the form
class Contactform(FlaskForm):
    #Contact form
    name = StringField("Name", [DataRequired()])
    email = StringField("Email", [Email(message=('Not a valid email address.')),DataRequired()])
    body = TextField("Message", [DataRequired(),Length(min=4,message="Message too short")])
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")