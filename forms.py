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


class MenuForm(FlaskForm):
    name = wtforms.StringField(
        label="Назва страви",
        validators=[wtforms.validators.length(max=500), wtforms.validators.DataRequired()]
    )
    description = wtforms.StringField(label="Опис (не обов'язково)", validators=[wtforms.validators.length(max=1000)])
    weight = wtforms.FloatField(label="Вага страви (не обов'язково)", default=None)
    ingredients = wtforms.StringField(label="Інгредієнти (не обов'язково)", validators=[wtforms.validators.length(max=500)])
    price = wtforms.FloatField(label="Ціна", validators=[wtforms.validators.DataRequired()])
    active = wtforms.BooleanField(label="Чи доступна страва", default=True)
    picture = wtforms.FileField(label="Фото страви (не обов'язково)", default=None)
    submit = wtforms.SubmitField(label="Додати страву")