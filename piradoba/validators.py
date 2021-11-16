from django.core.files.images import get_image_dimensions
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date

def img_resolution(value):
    w, h = get_image_dimensions(value)
    if w != 600 and h != 600:
        raise ValidationError("Image should be 600x600")

def Capital(value):
    if value[0].islower():
        raise ValidationError("First letter should be capital!")
def alpha(value):
    for i in value:
        if i.isalpha() == False:
            if i != " ":
                raise ValidationError("Wrong datatype!")
def all_upper(value):
    for letter in value:
        if letter.islower():
            raise ValidationError('Every letter should be uppercase!')

def gender_choices(value):
    if value != "male" and value != 'female':
        raise ValidationError('Answer should be lowercase male or female')

def personal_number_check(value):
    for i in value:
        if i.isnumeric() == False:
            raise ValidationError("Wrong datatype!")
        if len(value) != 11:
            raise ValidationError("Personal number requires 11 numbers!")

def check_date(value):
    today = date.today()
    if value > today:
        raise ValidationError('This date can\'t be in the future.')
def not_numeric(value):
    for i in value:
        if i.isnumeric():
            raise ValidationError("Wrong datatype!")