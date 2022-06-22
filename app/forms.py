from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    kullaniciadi = StringField('Kullanıcı Adı:',validators=[DataRequired()])
    sifre = PasswordField('Şifre',validators=[DataRequired()])
    beni_hatirla = BooleanField('Beni Hatırla')
    onayla = SubmitField('Giriş')
