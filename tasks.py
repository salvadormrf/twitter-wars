from celery import Celery

from analyser import check_spelling, find_city
from db import increment

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def analyse_tweet(text, geo):
    coordinates = geo.get("coordinates", [])
    if not coordinates:
        return
    
    res = check_spelling(text)
    
    valid_words = len(res["valid"])
    invalid_words = len(res["invalid"])
    #unchecked_words = len(res["unchecked"])
    
    city = find_city(coordinates)
    if not city:
        return
    
    increment("%s_valid_words" % city, valid_words)
    increment("%s_invalid_words" % city, invalid_words)
    increment("%s_tweets" % city, 1)
    
    return "City: %s Valid: %s Invalid: %s" % (city, valid_words, invalid_words)

