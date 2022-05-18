from atexit import register
from operator import ipow
from django import template
from mobilenumber.models import phonemodel, reviewmodel

register= template.Library()
@register.filter(name='mostdangerous')
def mostdangerous(phone_number):
    allusers= phonemodel.objects.filter(phone_number=phone_number)
    all_danger_reviews=reviewmodel.objects.filter(reviewnumber= allusers[0], review_status__icontains="danger")
    if allusers[0].status == 'DANGER' or  allusers[0].status == "danger":

        no_of_danger= len(all_danger_reviews)+1
        print('number of danger', no_of_danger)
    else:    
        no_of_danger= len(all_danger_reviews)
    return no_of_danger