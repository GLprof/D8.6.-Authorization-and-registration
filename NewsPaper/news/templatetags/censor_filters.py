from django import template

register = template.Library()

CENSOR_WORDS = ['яндекс', 'попса',]

@register.filter()
def censor(value):
    """
    value: post_text
    """
    words = value.split()
    for i in range(len(words)):
        if words[i].lower() in CENSOR_WORDS:
            words[i] = words[i][0] + '*' * (len(words[i]) - 1)
    return ' '.join(words)
