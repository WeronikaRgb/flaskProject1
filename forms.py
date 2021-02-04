from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class StworzGracza1(FlaskForm):
    username1 = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    username2 = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit1 = SubmitField('OK')

