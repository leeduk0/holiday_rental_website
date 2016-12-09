from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms import ValidationError
from wtforms.validators import InputRequired, DataRequired, Email


class CommentForm(FlaskForm):
    name = StringField('name', [InputRequired()])
    comment = TextAreaField('comment', [InputRequired()])


class BookingForm(FlaskForm):
    start_date = DateField('start_date', [DataRequired()], format='%d/%m/%Y', description='Start Date (DD/MM/YYYY)')
    end_date = DateField('end_date', [DataRequired()], format='%d/%m/%Y', description='End Date (DD/MM//YYYY)')
    name = StringField('name', [InputRequired()], description='Name')
    email = StringField('email', [InputRequired(), Email()], description='E-Mail')

    def validate_start_date(self, field):
        if self.start_date.data <= self.end_date.data:
            raise ValidationError(
                'Start date must be earlier than end date'
            )

    def validate_end_date(self, field):
        if self.end_date.data <= self.start_date.data:
            raise ValidationError(
                'End date must be later than start date.'
            )