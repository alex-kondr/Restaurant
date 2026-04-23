from flask_wtf import FlaskForm
import wtforms


class SignUpForm(FlaskForm):
    username = wtforms.StringField(
        label="Ваш логін",
        validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=3)]
    )
    password = wtforms.PasswordField(
        label="Пароль",
        validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=6)]
    )
    fullname = wtforms.StringField(label="ПІБ (не обов'язково)")
    email = wtforms.StringField(label="Email (не обов'зково)")
    submit = wtforms.SubmitField(label="Зареєструватись")


class SignInForm(FlaskForm):
    username = wtforms.StringField(
        label="Ваш логін",
        validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=3)]
    )
    password = wtforms.PasswordField(
        label="Пароль",
        validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=6)]
    )
    submit = wtforms.SubmitField(label="Вхід")