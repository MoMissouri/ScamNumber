from atexit import register
from django import template
from mobilenumber.models import phonemodel,reviewmodel

register= template.Library()
@register.filter(name='reviews')
def reviews(phone_number):
    review_number= phonemodel.objects.filter(phone_number=phone_number)
    if review_number.exists():
        all_reviews=reviewmodel.objects.filter(reviewnumber=review_number[0])
        return all_reviews
    return None