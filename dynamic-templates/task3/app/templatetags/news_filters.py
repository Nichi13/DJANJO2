from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    date = datetime.fromtimestamp(value)
    now = datetime.now()
    delta = now - date
    delta_minutes= delta.seconds / 60
    hours = int(delta_minutes / 60)
    format_date = datetime.fromtimestamp(value).strftime("%Y-%m-%d")
    if delta_minutes < 10:
        result = 'только что'
    elif hours < 1:
        result = '%s минут назад' %( int(delta_minutes))
    elif hours < 24:
        result = '%s часов назад' %(hours)
    elif hours >= 24:
        result = format_date
    return result

# необходимо добавить фильтр для поля `score`
@register.filter
def format_num_comments(value):
    if value == 0:
        result = 'Оставьте коментарий'
    elif 0 < value <= 50:
        result = value
    elif 50 < value:
        result = '50+'
    return result


@register.filter
def score(value):
    if value < -5:
        result = 'все плохо'
    elif  -5 <= value <= 5 :
        result = 'нейтрально'
    elif 5 < value:
        result = 'хорошо'
    return result


@register.filter
def format_selftext(value, count):
    text_len = len(value)
    if len(set(value.split())) >= 3:
        result = value[0:count]+'...'+value[(text_len-count):(text_len)]
    else:
        result = value
    return result

