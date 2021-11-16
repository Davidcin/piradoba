from django.db import models
from django.db.models import CharField, ImageField, DateField
from django.core.validators import RegexValidator
from .validators import img_resolution, gender_choices, Capital, all_upper, check_date, alpha, personal_number_check

# Create your models here.
class identity(models.Model):
    img = ImageField(upload_to='images/', validators=[img_resolution])
    first_name = CharField(max_length=10, validators=[Capital, alpha])
    last_name = CharField(max_length=24, validators=[Capital, alpha])
    citizen = CharField(max_length=3, validators=[all_upper, alpha])
    gender = CharField(default="" ,max_length=6, validators=[gender_choices])
    personal_number = CharField(primary_key=True, max_length=11, validators=[personal_number_check])
    birthday_date = DateField(validators=[check_date], default="YYYY-MM-DD")
    expiry_date = DateField(default="YYYY-MM-DD")
    birth_place = CharField(max_length=20, validators=[Capital, alpha])
    issue_date = DateField(validators=[check_date], default="YYYY-MM-DD")
