from datetime import datetime, date
from flask import request, redirect, url_for, render_template, flash, session
from portfolio import app
from portfolio.models.skil import Skil
from sqlalchemy import and_, or_
from functools import wraps

def login_required(view): 
    @wraps(view)
    def inner(*args, **kwargs): 
        if not session.get('logged_in'):
            return redirect(url_for('login')) 
        return view(*args, **kwargs) 
    return inner

@app.route('/', methods={'GET'})
def login():
    return render_template("login.html")

@app. route('/logout') 
def logout():
    session.pop('logged_in', None) 
    return redirect('/')

@app.route('/login', methods={'POST'})
def loginchk():
    ret=0
    if request.form['username'] != app.config['USERNAME']: 
        print(' ユーザ名が異なります') 
        ret=1
    elif request.form['password'] != app.config['PASSWORD']: 
        print(' パスワード が 異なります') 
        ret=2
    else: 
        session['logged_in'] = True
        return render_template("frame.html", sid=0) 

    return render_template("login.html", ret=ret)

@app.route('/<int:sid>', methods={'GET', 'POST'})
@login_required
def frame(sid):
    return render_template("frame.html", sid=sid)


@app.route('/search/<int:sid>', methods={'POST'})
@login_required
def search(sid):
    category = request.form.get("category")
    os = request.form.get("os")
    skil = request.form.get("skil")

    print("category:", category, "os:", os, "skil:", skil)
    if int(category) == 0:
        f = Skil.query
    else:    
        f = Skil.query.filter(Skil.category==int(category))
    if int(os) != 0:
        f = f.filter(Skil.os==int(os))
    if len(skil) >0:
        f = f.filter(Skil.skil.like("%{}%".format(skil)))
    skils = f.all()
    return render_template("skil_body.html", sid=sid, skils=skils)

@app.route('/left', methods={'GET', 'POST'})
@login_required
def left():
    return render_template("left.html")

@app.route('/welcome', methods={'GET', 'POST'})
@login_required
def welcome():
    return render_template("welcome.html")

@app.route('/head/<int:sid>', methods={'GET', 'POST'})
@login_required
def head(sid):
    head = "{}_head".format(get_menu(sid))
    return render_template("{}.html".format(head))

@app.route('/body/<int:sid>', methods={'GET', 'POST'})
@login_required
def body(sid):
    category = request.form.get("category")
    print("category", category)
    body = "{}_body".format(get_menu(sid))

    skils = Skil.query.all()
    return render_template("{}.html".format(body), skils=skils)

def get_menu(sid):
    if sid == 1:
        menu = "profile"
    elif sid == 2:
        menu = "career"
    elif sid == 3:
        menu = "skil"
    else:
        menu = "user"
    return menu
