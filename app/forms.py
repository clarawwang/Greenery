from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class DailyForm(FlaskForm):
    week = IntegerField("What week is it?", validators=[DataRequired()], default=1)
    berry = IntegerField("Servings", validators=[DataRequired()], default=0)
    avocado = IntegerField("Servings", validators=[DataRequired()], default=0)
    tomato = IntegerField("Servings", validators=[DataRequired()], default=0)
    banana =IntegerField("Servings", validators=[DataRequired()], default=0)
    apple = IntegerField("Servings", validators=[DataRequired()], default=0)
    citrus = IntegerField("Servings", validators=[DataRequired()], default=0)
    beef = IntegerField("Servings", validators=[DataRequired()], default=0)
    lamb = IntegerField("Servings", validators=[DataRequired()], default=0)
    prawn =IntegerField("Servings", validators=[DataRequired()], default=0)
    fish = IntegerField("Servings", validators=[DataRequired()], default=0)
    pork = IntegerField("Servings", validators=[DataRequired()], default=0)
    chicken = IntegerField("Servings", validators=[DataRequired()], default=0)
    cheese = IntegerField("Servings", validators=[DataRequired()], default=0)
    egg = IntegerField("Servings", validators=[DataRequired()], default=0)
    tofu = IntegerField("Servings", validators=[DataRequired()], default=0)
    bean = IntegerField("Servings", validators=[DataRequired()], default=0)
    pea = IntegerField("Servings", validators=[DataRequired()], default=0)
    nut = IntegerField("Servings", validators=[DataRequired()], default=0)
    rice = IntegerField("Servings", validators=[DataRequired()], default=0)
    pasta = IntegerField("Servings", validators=[DataRequired()], default=0)
    oat = IntegerField("Servings", validators=[DataRequired()], default=0)
    bread = IntegerField("Servings", validators=[DataRequired()], default=0)
    potato = IntegerField("Servings", validators=[DataRequired()], default=0)
    milk = IntegerField("Servings", validators=[DataRequired()], default=0)
    pl_milk = IntegerField("Servings", validators=[DataRequired()], default=0)
    beer = IntegerField("Servings", validators=[DataRequired()], default=0)
    coffee = IntegerField("Servings", validators=[DataRequired()], default=0)
    wine = IntegerField("Servings", validators=[DataRequired()], default=0)
    tea = IntegerField("Servings", validators=[DataRequired()], default=0)

    ecar = IntegerField("Miles Traveled", validators=[DataRequired()], default=0)
    gcar = IntegerField("Miles Traveled", validators=[DataRequired()], default=0)
    train = IntegerField("Miles Traveled", validators=[DataRequired()], default=0)
    bus =  IntegerField("Miles Traveled", validators=[DataRequired()], default=0)
    plane =  IntegerField("Miles Traveled", validators=[DataRequired()], default=0)

    gas = IntegerField("Dollars", validators=[DataRequired()], default=0)
    electricity = IntegerField("Dollars", validators=[DataRequired()], default=0)
    fuel = IntegerField("Dollars", validators=[DataRequired()], default=0)
    propane = IntegerField("Dollars", validators=[DataRequired()], default=0)

    submit = SubmitField('Enter Info')

class ReductionForm(FlaskForm):
    up = IntegerField("input degrees", validators=[DataRequired()], default=0)
    down = IntegerField("input degrees", validators=[DataRequired()], default=0)
    light =IntegerField("input lights", validators=[DataRequired()], default=0)
    power = BooleanField("Will enable features")
    green = IntegerField("input percent", validators=[DataRequired()], default=0)
    wash = IntegerField("input loads", validators=[DataRequired()], default=0)
    dry = IntegerField("input percent", validators=[DataRequired()], default=0)
    fridge = BooleanField("Will replace")
    furnace = BooleanField("Will replace")
    windows = BooleanField("Will replace")
    main = BooleanField("Will maintain")
    gcar = IntegerField("number miles", validators=[DataRequired()], default=0)
    ecar = IntegerField("number miles", validators=[DataRequired()], default=0)
    bus = IntegerField("umber miles", validators=[DataRequired()], default=0)
    train = IntegerField("number miles", validators=[DataRequired()], default=0)
    plane = IntegerField("number miles", validators=[DataRequired()], default=0)
    submit = SubmitField('Enter Info')
  
    