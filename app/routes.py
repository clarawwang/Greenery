from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app.models import User, UserInfo
from flask_login import logout_user
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm, DailyForm
from flask_login import login_required

@app.route('/')

@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/Daily/<username>', methods=['GET', 'POST'])
@login_required
def Daily(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = DailyForm()
    if request.method == "POST":
        berry = int(form.berry.data)
        avocado = int(form.avocado.data)
        tomato = int(form.tomato.data)
        banana = int(form.banana.data)
        apple = int(form.apple.data)
        citrus = int(form.citrus.data)
        beef = int(form.beef.data)
        lamb = int(form.lamb.data)
        prawn = int(form.prawn.data)
        fish = int(form.fish.data)
        pork = int(form.pork.data)
        chicken = int(form.chicken.data)
        cheese = int(form.cheese.data)
        egg =int(form.egg.data)
        tofu = int(form.tofu.data)
        bean = int(form.bean.data)
        pea = int(form.pea.data)
        nut = int(form.nut.data)
        rice = int(form.rice.data)
        pasta = int(form.pasta.data)
        oat = int(form.oat.data)
        bread = int(form.bread.data)
        potato = int(form.potato.data)
        milk = int(form.milk.data)
        pl_milk = int(form.pl_milk.data)
        beer = int(form.beer.data)
        coffee = int(form.coffee.data)
        wine = int(form.wine.data)
        tea = int(form.tea.data)
        ecar = int(form.ecar.data)
        gcar = int(form.gcar.data)
        train = int(form.train.data)
        bus =  int(form.bus.data)
        plane =  int(form.plane.data)
        gas = int(form.gas.data)
        electricity = int(form.electricity.data)
        fuel = int(form.fuel.data)
        propane = int(form.propane.data)
        week  = int(form.week.data)

        ##calc home energy ##
        enCoeff={"gas":2.8, "elec":1.3, "fuel":67/3, "propane":60/3}
        enTotal = enCoeff["gas"] * gas + enCoeff["elec"] * electricity + enCoeff["fuel"]*fuel + enCoeff["propane"] * propane
        enTotal //= 4

        ##calc Transport ##
        transCo = {"gcar":1.05, "ecar":2.48, "train":(1/3), "plane":0.5}
        transTotal = int(transCo["gcar"]*gcar + transCo["ecar"]*ecar + transCo["train"]*train + transCo["plane"]*plane)

        #food calc##
        foodList = [berry, avocado, tomato, banana, apple, citrus, beef, lamb,
        prawn, fish, pork, chicken, cheese, egg, tofu,bean, pea, nut, rice, pasta, oat,
        bread, potato, milk, pl_milk, beer,coffee, wine,tea]
        foodName = ["berry", "avocado", "tomato", "banana", "apple", "citrus", "beef", "lamb",
        "prawn", "fish", "pork", "chicken", "cheese", "egg", "tofu","bean", "pea", "nut", "rice", "pasta", "oat",
        "bread", "potato", "milk", "pl_milk", "beer","coffee", "wine","tea"]
        foodDict = {"berry":0.24, "avocado":0.39, "tomato":0.33, "banana":0.13, "apple":0.07, "citrus":0.065,
        "beef":15.43, "lamb":8.47, "prawn":6.68, "fish":3.84, "pork":3.67, "chicken":3.18, "cheese":2.27, 
        "egg":1.58, "tofu":0.47, "bean":0.22, "pea":0.07, "nut":0.04, "rice":0.73, "pasta":0.26, "oat":0.20,
        "bread":0.14, "potato":0.12, "milk":1.35, "pl_milk": 0.41, "beer":1.41, "coffee":0.92, "wine":0.68,
        "tea":0.87}
        foodOut = 0
        for i in range(len(foodList)):
            foodOut += foodDict[foodName[i]] * foodList[i]

        foodOut = int(foodOut)
        out = foodOut + transTotal + enTotal
        #bf1=bf1, bf2=bf2, bf3=bf3,lf1=lf1,lf2=lf2,df1=df1, df2=df2, df3=df3, transport=tn1,distance=ta1, enSource=et1, enAmt=ea1,
        info = UserInfo(berry=berry, avocado=avocado, tomato=tomato, banana=banana, apple=apple, 
        citrus=citrus, beef=beef, lamb=lamb,
        prawn=prawn, fish=fish, pork=pork, chicken=chicken, cheese=cheese, egg=egg, tofu =tofu,bean=bean, pea=pea, nut=nut, rice=rice, pasta=pasta, oat=oat,
        bread=bread, potato=potato, milk=milk, pl_milk=pl_milk, beer=beer,coffee=coffee, wine=wine,tea=tea,
        ecar=ecar, gcar=gcar,train=train,bus=bus,plane=plane,gas=gas, electricity=electricity, fuel=fuel, propane=propane,
        user = current_user.username, totalOut=out, foodOut =foodOut, enOut=enTotal, week = week, transOut = transTotal, author = current_user)
        db.session.add(info)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('dailyform.html', title='Fill In Your Daily Info', form=form)

from flask import Markup

@app.route('/Analysis/<username>', methods=['GET', 'POST'])
@login_required
def Analysis(username):
    user = User.query.filter_by(username=username).first_or_404()
    data = UserInfo.query.filter_by(user=current_user.username)
    data = data[-1]
    label = ["Food Total", "Energy Total", "Transport Total"]
    values = [data.foodOut, data.enOut, data.transOut]
    enCoeff={"gas":134/3, "elec":62/3, "fuel":67/3, "propane":60/3}
    
    colors = [ "#F7464A", "#46BFBD", "#FDB45C"]
    enAvg = [201.5, 155, 1212//3, 561//3]
    transAvg = [265]
    foodAvg = [250]
    natAvg = [768//3, 1364//3, 1212//3, 561//3, 265, 250]
    avgVal = [data.gas * enCoeff["gas"], data.electricity * enCoeff["elec"], data.fuel * enCoeff["fuel"], data.propane * enCoeff["propane"], data.transOut, data.foodOut]
    avgLabel = ["Gas", "Electricity", "Fuel Oil", "Propane", "Transport", "Food"]
    #print(labels, values,colors)
    return render_template('analysis.html', week = data.week, avglabel = avgLabel, natAvg = natAvg, avgVal=avgVal, values=values, label=label, colors=colors)
    #return render_template('analysis.html', title='Your Daily Info', data=data)


