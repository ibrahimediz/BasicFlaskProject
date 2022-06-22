from turtle import title
from app import app
from flask import render_template

from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {"kullanici":"Uzaktan"}
    gonderiler = [
    {
        "yazar":"Limasollu Naci",
        "içerik":"Donat Donat Donat"
    },
    {
        "yazar":"Kaşgarlı Mahmut",
        "içerik":"Divan-ı Lugat Türk"
    },
        {
        "yazar":"Kaşgarlı Mahmut",
        "içerik":"Divan-ı Lugat Türk"
    },
        {
        "yazar":"Kaşgarlı Mahmut",
        "içerik":"Divan-ı Lugat Türk"
    }]
    return render_template("index.html",user=user,gonderiler=gonderiler)
        
@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html",baslik="Giriş Yap",form=form)


