from django import template
import itertools

register = template.Library()

@register.simple_tag
def set_var(qset, pos, elem):
	
    return str('images/'+str(qset.filter(f_card_no=pos).values(elem)[0][elem])+'.png')

@register.simple_tag
def set_common(qset, card1, card2):
    elem1 = qset.filter(f_card_no=card1).values_list()
    a = str(list(elem1)[0])
    a = a.replace("'","")
    a1 = a.split(',')[2:10]
    
    elem2 = qset.filter(f_card_no=card2).values_list()
    b = str(list(elem2)[0])
    b = b.replace("'","")
    b1 = b.split(',')[2:10]
    c = set(a1) & set(b1)
    return [str(list(c)[0]).strip()]

@register.simple_tag
def check_common(common, clicked):
    clicked1 = clicked.lstrip('\\')
    clicked2 = clicked1.rstrip('.')
    return clicked

@register.simple_tag
def get_card(qset, card_no):
    card = list(qset.filter(f_card_no=card_no).values_list()[0])
    return card