from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed  # ✅ Add this import
from wtforms import StringField, EmailField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[
        DataRequired(), 
        Regexp(r'^\+?[0-9\s-]+$', message="Invalid phone number format"),
        Length(min=10, max=15)
    ])
    dob = DateField("Date of Birth", validators=[DataRequired()], format='%Y-%m-%d')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ApplicantForm(FlaskForm):  
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[
        DataRequired(), 
        Regexp(r'^\+?[0-9\s-]+$', message="Invalid phone number format"),
        Length(min=10, max=15)
    ])
    submit = SubmitField('Submit')

class FamilyDetailsForm(FlaskForm):
    father_name = StringField('Father Name', validators=[DataRequired(), Length(min=2, max=50)])
    mother_name = StringField('Mother Name', validators=[DataRequired(), Length(min=2, max=50)])
    guardian_name = StringField('Guardian Name (if applicable)', validators=[Optional(), Length(max=50)])
    submit = SubmitField('Submit')

class BankDetailsForm(FlaskForm):
    account_number = StringField('Account Number', validators=[DataRequired(), Length(min=8, max=20)])
    ifsc_code = StringField('IFSC Code', validators=[DataRequired(), Length(min=5, max=15)])
    bank_name = StringField('Bank Name', validators=[DataRequired(), Length(min=2, max=50)])
    branch_name = StringField('Branch Name', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Submit')

class DocumentUploadForm(FlaskForm):
    document = FileField('Upload Document', validators=[
        DataRequired(), 
        FileAllowed(['pdf', 'jpg', 'png', 'jpeg'], 'Only PDF, JPG, PNG, and JPEG files are allowed!')
    ])  # ✅ Allow only specific file types
    submit = SubmitField('Submit')
